import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton("Open File Dialog", self)
        self.button.clicked.connect(self.showCustomFileDialog)
        self.button.setGeometry(150, 80, 200, 30)

    def showCustomFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # To make the selected file read-only

        file_dialog = QFileDialog()
        file_dialog.setOptions(options)

        file_dialog.setWindowTitle("Custom File Dialog")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        filter_text = "Text files (*.txt)"
        filter_images = "Image files (*.png *.jpg *.jpeg *.gif)"
        filter_videos = "Video files (*.mp4 *.avi *.mkv)"
        filter_sounds = "Sound files (*.mp3 *.wav)"

        file_dialog.setNameFilter(filter_text + ";;" + filter_images + ";;" + filter_videos + ";;" + filter_sounds)

        if file_dialog.exec_():
            file_name = file_dialog.selectedFiles()[0]
            print("Selected file:", file_name)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
