import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QVBoxLayout, QWidget, QScrollArea


class ServerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Server")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        title_label = QLabel("Server")
        title_label.setStyleSheet('color: #007AFF; font-size: 30px')
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet('color: green; font-size: 16px')
        scroll_area.setWidget(self.text_edit)

    def add_text(self, text):
        self.text_edit.append(text)


def main():
    app = QApplication(sys.argv)
    window = ServerGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
