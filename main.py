from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec())
