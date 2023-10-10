import sys

import qdarktheme
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QStackedWidget, \
    QHBoxLayout, QScrollArea, QListWidget, QListWidgetItem, QFileDialog, QMessageBox, QProgressBar

from src.gui.client.download_page import DownloadPage
from src.gui.client.main_menu_page import MainMenuPage
from src.gui.client.upload_page import UploadPage


class ClientGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.menu_page = MainMenuPage(self)
        self.download_page = DownloadPage(self)
        self.upload_page = UploadPage(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("ServerFileSystem")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.stacked_widget = QStackedWidget()

        central_layout = QVBoxLayout()
        central_layout.addWidget(self.stacked_widget)

        central_widget.setLayout(central_layout)

        self.stacked_widget.addWidget(self.menu_page)

        self.stacked_widget.addWidget(self.download_page)

        self.stacked_widget.addWidget(self.upload_page)

    def download(self):
        self.stacked_widget.setCurrentWidget(self.download_page)

    def upload(self):
        self.stacked_widget.setCurrentWidget(self.upload_page)

    def show_menu(self):
        self.stacked_widget.setCurrentWidget(self.menu_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    window = ClientGUI()
    window.show()

    sys.exit(app.exec_())
