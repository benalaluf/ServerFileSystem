from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem, QPushButton, QScrollArea, QLabel, QVBoxLayout, QWidget, \
    QListWidget


class DownloadPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.chosen_file = 'None'
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.layout)

        download_label = QLabel("Download")
        download_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        download_label.setStyleSheet("font-family:Ariel; font-size: 34px; color: #007AFF;")
        self.layout.addWidget(download_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        self.list_widget = QListWidget()
        self.scroll_area.setWidget(self.list_widget)

        self.list_widget.itemClicked.connect(self.on_item_clicked)

        self.download_button = QPushButton("Download")
        self.download_button.setStyleSheet("background-color: #007AFF; color: white; font-size: 18px; "
                                           "border-radius: 10px;")
        self.download_button.setToolTip("Download the selected file")
        self.download_button.clicked.connect(self.download)
        self.download_button.setFixedHeight(35)  # Increase button height

        self.layout.addWidget(self.download_button)

        self.back_button = QPushButton("Back to Menu")
        self.back_button.setStyleSheet("font-size: 18px; border-radius: 10px; color: #ffffff")
        self.back_button.clicked.connect(self.parent.show_menu)
        self.layout.addWidget(self.back_button)

    def add_item(self, text: str):
        item = QListWidgetItem(text)
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsSelectable)
        self.list_widget.addItem(item)

    def download(self):
        if self.chosen_file:
            QMessageBox.information(self, "Download Complete", f"Downloaded: {self.chosen_file}")

    def on_item_clicked(self, item):
        clicked_text = item.text()
        self.chosen_file = clicked_text
