import sys
import threading

from PyQt5.QtWidgets import QApplication

from src.connections.client import ClientConn
from src.gui.client.client_gui import ClientGUI
import qdarktheme

from src.protocol.protocol import Packet, PacketType


class ClientApp(ClientConn):
    def __init__(self, ip, port, file_path):
        super().__init__(ip, port, file_path)
        self.app = QApplication(sys.argv)
        qdarktheme.setup_theme()
        self.client_gui = ClientGUI()

        self._connect_back_to_front()

    # override
    def handle_packet(self, packet: Packet):
        super().handle_packet(packet)
        if packet.packet_type == PacketType.SHOW:
            self.display_avalibale_server_files(packet.file_name.split('\n'))

    def _connect_back_to_front(self):
        self.__connect_download_button()
        self.__connect_upload_button()
        self.__connect_menu_download_button()

    def download(self):

        self.get(self.client_gui.download_page.chosen_file)

    def upload(self):
        print("uploading")
        self.send_file(self.client_gui.upload_page.chosen_file)

    def display_avalibale_server_files(self, list):
        self.client_gui.download_page.list_widget.clear()
        for item in list:
            self.client_gui.download_page.add_item(item)

    def __connect_menu_download_button(self):
        self.client_gui.menu_page.download_button.clicked.connect(self._list_server_files)

    def __connect_download_button(self):
        download_button = self.client_gui.download_page.download_button
        download_button.clicked.connect(self.download)

    def __connect_upload_button(self):
        upload_button = self.client_gui.upload_page.upload_button
        upload_button.clicked.connect(self.upload)

    def run(self):
        self.client_gui.show()
        sys.exit(self.app.exec_())

    def main(self):
        threading.Thread(super().main())
        self.run()


if __name__ == '__main__':
    ClientApp('0.0.0.0', 6980, '/Users/blu/Desktop/client').main()
