import os
import socket
import threading
from abc import ABC

from src.protocol.protocol import *
from src.utils.commmad_invoker import CommandInvoker


class ClientConn(ABC):
    def __init__(self, ip, port, file_path):
        self.ip = ip
        self.port = port
        self.addr = (ip, port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.file_path = file_path

        self.connect()


    def main(self):
        threading.Thread(target=self.handle_server).start()

    def connect(self):
        self.client.connect(self.addr)
        print(f"CONNECTED TO {self.addr}")

    def handle_server(self):
        while True:
            packet = HandelPacket.recv_packet(self.client)
            self.handle_packet(packet)

    def handle_packet(self, packet: Packet):
        if packet.packet_type == PacketType.GET:
            print(f"Got File From {self.client}")
            self.recv_file(packet)



    def recv_file(self, packet: Packet):
        self.__write_file(packet.file_name, packet.file_data)

    def get(self, file_name):
        SendPacket.send_packet(self.client, Packet(PacketType.GET, file_name, PacketConstants.NO_DATA))

    def send_file(self, file_name):
        name, data = self.__read_file(file_name)
        packet = Packet(PacketType.PUT, name, data)
        SendPacket.send_packet(self.client, packet)
        print('sent file')

    def __write_file(self, file_name: str, file_data: bytes):
        with open(f'{self.file_path}/{file_name}', 'wb') as f:
            f.write(file_data)

    def __read_file(self, file_name: str):
        try:
            with open(file_name, 'rb') as f:
                file_data = f.read()

            file_name = file_name.split('/')[-1]
            return file_name, file_data
        except FileNotFoundError:
            print("file not found")

    def __list_files(self):
        files = os.listdir(self.file_path)
        for file in files:
            print(file)

    def _list_server_files(self):
        SendPacket.send_packet(self.client, Packet(PacketType.SHOW,'NO_DATA', PacketConstants.NO_DATA))
