import os
import socket
import threading

from src.protocol.protocol import *


class Server:

    def __init__(self, ip, port, file_path):
        self.ip = ip
        self.port = port
        self.addr = (ip, port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.addr)
        self.file_path = file_path

    def main(self):
        self.start_listening()

    def start_listening(self):
        self.server.listen()
        print(f"Listening.... {self.addr}")
        while True:
            conn, addr = self.server.accept()
            print(f'got connectoin from {conn}')
            threading.Thread(target=self.handle_client, args=(conn,)).start()

    def handle_client(self, conn):
        while True:
            packet = HandelPacket.recv_packet(conn)
            self.handle_packet(packet, conn)

    def handle_packet(self, packet: Packet, conn: socket.socket):
        print('got packet', packet.packet_type)
        if packet.packet_type == PacketType.GET:
            print(f'Send {packet.file_name} {conn.getpeername()}')
            self.send_file(packet, conn)

        if packet.packet_type == PacketType.PUT:
            print(f"Got {packet.file_name} {conn.getpeername()}")
            self.recv_file(packet)

        if packet.packet_type == PacketType.SHOW:
            self.send_list_files(conn)

    def recv_file(self, packet: Packet):
        self.__write_file(packet.file_name, packet.file_data)

    def send_file(self, packet: Packet, conn):
        name, data = self.__read_file(packet.file_name)
        packet = Packet(PacketType.GET, name, data)
        SendPacket.send_packet(conn, packet)

    def __write_file(self, file_name: str, file_data: bytes):
        with open(f'{self.file_path}/{file_name}', 'wb') as f:
            f.write(file_data)

    def __read_file(self, file_name: str):
        with open(f'{self.file_path}/{file_name}', 'rb') as f:
            file_data = f.read()

        return file_name, file_data

    def send_list_files(self, conn):
        print(f'sending show to {conn}')
        files = os.listdir(self.file_path)

        files = "\n".join(files)

        packet = Packet(PacketType.SHOW, files, PacketConstants.NO_DATA)
        SendPacket.send_packet(conn, packet)
