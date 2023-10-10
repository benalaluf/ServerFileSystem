from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QProgressBar, \
    QMessageBox


class UploadPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.chosen_file = None
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
        chose_file_button = QPushButton("Choose File")
        chose_file_button.setStyleSheet("font-size: 18px;border-radius: 10px; color: #ffffff;")
        chose_file_button.clicked.connect(self.showCustomFileDialog)
        chose_file_button.setFixedHeight(35)  # Increase button height
        chose_file_layout.addWidget(chose_file_button)
        self.file_label = QLabel(self.chosen_file)
        chose_file_layout.addWidget(self.file_label)

        self.layout.addLayout(chose_file_layout)

        upload_button = QPushButton("Upload")
        upload_button.setStyleSheet("background-color: #4CD964; color: white; font-size: 18px; "
                                    "border-radius: 10px;")
        upload_button.setToolTip("Upload the selected file")
        upload_button.clicked.connect(self.upload)
        upload_button.setFixedHeight(35)  # Increase button height
        self.layout.addWidget(upload_button)

        self.layout.addStretch(1)
        back_button = QPushButton("Back to Menu")
        back_button.setStyleSheet(
            "font-size: 18px;border-radius: 10px; color: #ffffff;")  # Removed background-color style
        back_button.setToolTip("Return to the main menu")
        back_button.clicked.connect(self.parent.show_menu)
        self.layout.addWidget(back_button)

    def showCustomFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # To make the selected file read-only

        file_dialog = QFileDialog()
        file_dialog.setOptions(options)

        file_dialog.setWindowTitle("Custom File Dialog")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        filter_text = "Text files (*.txt);;All files (*)"
        file_dialog.setNameFilter(filter_text)

        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            print("Selected file:", file_name)
            self.chosen_file = file_name
            self.file_label.setText(self.chosen_file)

    def upload(self):
        if self.chosen_file:
            QMessageBox.information(self, "Upload Complete", f"Uploaded: {self.chosen_file}")
