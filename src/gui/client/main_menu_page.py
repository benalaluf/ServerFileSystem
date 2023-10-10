from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton


class MainMenuPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

        title_label = QLabel("ServerFileSystem")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 36px;")  # Adjust the font size
        layout.addWidget(title_label)

        layout.addSpacing(150)

        button_layout = QHBoxLayout()
        self.download_button = QPushButton("Download")
        self.download_button.setStyleSheet("background-color: #007AFF; color: white; font-size: 24px; "
                                      "border-radius: 10px;")
        self.download_button.setToolTip("Download files from the server")
        self.download_button.clicked.connect(self.parent.download)
        self.download_button.setFixedHeight(80)  # Increase button height
        button_layout.addWidget(self.download_button)

        upload_button = QPushButton("Upload")
        upload_button.setStyleSheet("background-color: #4CD964; color: white; font-size: 24px; "
                                    "border-radius: 10px;")
        upload_button.setToolTip("Upload files to the server")
        upload_button.clicked.connect(self.parent.upload)
        upload_button.setFixedHeight(80)  # Increase button height
        button_layout.addWidget(upload_button)

        layout.addLayout(button_layout)
