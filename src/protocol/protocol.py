import socket
import struct
from enum import Enum


class PacketConstants:
    TYPE_HEADER_FORMAT = '>B'  # big-big-endian unsigned char
    PAYLOAD_LENGTH_HEADER_FORMAT = '>I'  # big-endian unsigned int
    HEADER_LENGTH = 9  # bytes
    NO_DATA = 'NO_DATA'.encode()
    # 1 byte packet type \ 4 byte file_name_len \ 4 byte file_data_len\ file_name \ file_data


class PacketType(Enum):
    PUT = 1
    GET = 2
    SHOW = 3


class Packet:
    def __init__(self, packet_type: PacketType, file_name: str, file_data: bytes):
        self.packet_type = packet_type
        self.file_name = file_name
        self.file_name_bytes = file_name.encode()
        self.file_data = file_data
        self.packet_bytes = bytes()

    @classmethod
    def from_bytes(cls, data: bytearray):
        packet_type = struct.unpack(PacketConstants.TYPE_HEADER_FORMAT, bytes(data[0:1]))[0]
        name_len = struct.unpack(PacketConstants.PAYLOAD_LENGTH_HEADER_FORMAT, bytes(data[1:5]))[0]
        data_len = struct.unpack(PacketConstants.PAYLOAD_LENGTH_HEADER_FORMAT, bytes(data[5:9]))[0]
        name = bytes(data[9:9 + name_len])
        data = bytes(data[9 + name_len:])

        return cls(PacketType(packet_type), name.decode(), data)

    def __bytes__(self):
        return self._build_packet()

    def _build_packet(self):
        self.packet_bytes = self._pack(PacketConstants.TYPE_HEADER_FORMAT, self.packet_type.value) + \
                            self._pack(PacketConstants.PAYLOAD_LENGTH_HEADER_FORMAT, (len(self.file_name_bytes))) + \
                            self._pack(PacketConstants.PAYLOAD_LENGTH_HEADER_FORMAT, (len(self.file_data))) + \
                            self.file_name_bytes + \
                            self.file_data
        return self.packet_bytes

    def _pack(self, pack_format: str, data):
        return struct.pack(pack_format, data)


class SendPacket:

    @staticmethod
    def send_packet(sock: socket.socket, packet: Packet):
        sock.sendall(bytes(packet))
        # print('sent packet')


class HandelPacket:

    @staticmethod
    def recv_packet(sock):
        return Packet.from_bytes(HandelPacket.__recv_raw_packet(sock))

    @staticmethod
    def __recv_raw_packet(sock):
        # print('start recving')
        raw_header = HandelPacket.__recv_all(sock, PacketConstants.HEADER_LENGTH)
        # print(f'recved raw header {raw_header}')

        if not raw_header:
            return None

        raw_name_len = raw_header[1:5]
        name_len = struct.unpack(PacketConstants.PAYLOAD_LENGTH_HEADER_FORMAT, raw_name_len)[0]
        name = HandelPacket.__recv_all(sock, name_len)
        # print(f'revd file name {name.decode()}')

        raw_data_len = raw_header[5:9]
        data_len = struct.unpack(PacketConstants.PAYLOAD_LENGTH_HEADER_FORMAT, raw_data_len)[0]
        data = HandelPacket.__recv_all(sock, data_len)
        # print("recv data")

        return raw_header + name + data

    @staticmethod
    def __recv_all(sock, data_len):
        data = bytearray()
        while len(data) < data_len:
            packet = sock.recv(data_len - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data
