import psutil
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QProgressBar, \
    QMessageBox


class UploadPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.chosen_file = 'None'
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Center the buttons vertically
        self.setLayout(self.layout)

        upload_label = QLabel("Upload")
        upload_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        upload_label.setStyleSheet(
            "font-family:Arial ;font-size: 36px; color: #4CD964;")  # Adjust the font size and color
        self.layout.addWidget(upload_label)

        self.layout.addSpacing(100)

        chose_file_layout = QHBoxLayout()

        chose_file_button_layout = QHBoxLayout()
        chose_file_button = QPushButton("Choose File")
        chose_file_button.setStyleSheet("font-size: 18px;border-radius: 10px; color: #ffffff;")
        chose_file_button.clicked.connect(self.file_dialog)
        chose_file_button.setFixedHeight(35)  # Increase button height
        chose_file_button_layout.addWidget(chose_file_button)

        chose_file_button_from_usb = QPushButton("from usb")
        chose_file_button_from_usb.setStyleSheet("font-size: 14px;border-radius: 10px; color: #ffffff;")
        chose_file_button_from_usb.clicked.connect(self.upload_from_usb)
        chose_file_button_from_usb.setFixedHeight(35)
        chose_file_button_from_usb.setFixedWidth(80)  # Increase button height
        chose_file_button_layout.addWidget(chose_file_button_from_usb)
        chose_file_layout.addLayout(chose_file_button_layout)
        self.file_label = QLabel(self.chosen_file)
        chose_file_layout.addWidget(self.file_label)

        self.layout.addLayout(chose_file_layout)

        self.upload_button = QPushButton("Upload")
        self.upload_button.setStyleSheet("background-color: #4CD964; color: white; font-size: 18px; "
                                         "border-radius: 10px;")
        self.upload_button.setToolTip("Upload the selected file")
        self.upload_button.clicked.connect(self.upload)
        self.upload_button.setFixedHeight(35)  # Increase button height
        self.layout.addWidget(self.upload_button)

        self.layout.addStretch(1)
        back_button = QPushButton("Back to Menu")
        back_button.setStyleSheet(
            "font-size: 18px;border-radius: 10px; color: #ffffff;")  # Removed background-color style
        back_button.setToolTip("Return to the main menu")
        back_button.clicked.connect(self.parent.show_menu)
        self.layout.addWidget(back_button)

    def is_usb(self):
        for partition in psutil.disk_partitions():
            if 'removable' in partition.opts or 'usb' in partition.opts:
                return True
        return False

    def upload_from_usb(self):
        if self.is_usb():
            for partition in psutil.disk_partitions():
                if 'removable' in partition.opts or 'usb' in partition.opts:
                    self.usb_file_dialog(partition.device)
        else:
            if self.chosen_file:
                QMessageBox.information(self, "no usb", f"no usb detected: {self.chosen_file}")

    def usb_file_dialog(self, path):
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("USB Stick Detected")
        file_dialog.setFileMode(QFileDialog.Directory)
        file_dialog.setOption(QFileDialog.ReadOnly, True)
        file_dialog.setDirectory(path)

        result = file_dialog.exec_()
        if result == QFileDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                selected_directory = selected_files[0]
                self.chosen_file =selected_directory

    def file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # To make the selected file read-only

        file_dialog = QFileDialog()
        file_dialog.setOptions(options)

        file_dialog.setWindowTitle("Custom File Dialog")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        filter_text = "Text files (.txt)"
        filter_images = "Image files (.png .jpg.jpeg .gif)"
        filter_videos = "Video files (.mp4 .avi.mkv)"
        filter_sounds = "Sound files (.mp3.wav)"

        file_dialog.setNameFilter(filter_text + ";;" + filter_images + ";;" + filter_videos + ";;" + filter_sounds)

        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            print("Selected file:", file_name)
            self.chosen_file = file_name
            self.file_label.setText(self.chosen_file)

    def upload(self):
        if self.chosen_file:
            QMessageBox.information(self, "Upload Complete", f"Uploaded: {self.chosen_file}")
