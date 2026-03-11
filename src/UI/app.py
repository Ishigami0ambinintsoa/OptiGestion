import sys

from PyQt6.QtWidgets import QMainWindow, QGridLayout,QVBoxLayout,QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        def initUI(self):
            grid = QGridLayout()
            self.setCentralWidget(grid)
            self.setWindowTitle("Hello World")
            self.setGeometry(300, 300, 250, 150)
            self.show()

app = MyWindow

app.exec()