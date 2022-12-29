from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class UI(QWidget):
    def __init__(self):
        app = QApplication(sys.argv)
        super(UI,self).__init__()
        self.setWindowTitle("University Tool Helper")
        
        grid = QGridLayout()

        self.setLayout(grid)
        self.show()
        sys.exit(app.exec())