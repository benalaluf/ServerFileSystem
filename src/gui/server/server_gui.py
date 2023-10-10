import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QVBoxLayout, QWidget, QScrollArea

class ScrollableTextPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scrollable Text Page")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        # Title Label
        title_label = QLabel("Server").setStyleSheet('color: blue;')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Scrollable Text Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        text_edit = QTextEdit()
        text_edit.setPlainText("This is a scrollable text area.\n" * 50)  # Sample text
        scroll_area.setWidget(text_edit)

def main():
    app = QApplication(sys.argv)
    window = ScrollableTextPage()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
