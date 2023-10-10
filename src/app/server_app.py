import sys
import threading

import qdarktheme
from PyQt5.QtWidgets import QApplication

from src.connections.server import Server
from src.gui.server.server_gui import ServerGUI
from src.protocol.protocol import *


class ServerApp(Server):
    def __init__(self, ip, port, path):
        super().__init__(ip, port, path)
        self.app = QApplication(sys.argv)
        qdarktheme.setup_theme()
        self.server_gui = ServerGUI()

    def main(self):
        threading.Thread(target=super().main).start()
        self.run_gui()

    #override
    def handle_packet(self, packet: Packet, conn: socket.socket):
        if packet.packet_type == PacketType.GET:
            self.server_gui.add_text(f'Send {packet.file_name} From {conn.getpeername()}')
            self.send_file(packet, conn)

        if packet.packet_type == PacketType.PUT:
            self.server_gui.add_text(f"Got {packet.file_name} From {conn.getpeername()}")
            self.recv_file(packet)

        if packet.packet_type == PacketType.SHOW:
            self.send_list_files(conn)

    def run_gui(self):
        self.server_gui.show()
        sys.exit(self.app.exec_())
