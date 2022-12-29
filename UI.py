from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class UI:
    def __init__(self) -> None:
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle("University Tool Helper")
        window.show()
        sys.exit(app.exec())
    