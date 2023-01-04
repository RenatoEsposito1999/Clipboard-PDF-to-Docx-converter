from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import QSize



def initBar():
    global progressiveBar
    progressiveBar = QProgressBar()
    progressiveBar.setFixedSize(QSize(230, 30))
    progressiveBar.setValue(0)
    return progressiveBar

def clearProgress():
    progressiveBar.setValue(0)

def updateValue(value):
    if int(progressiveBar.value()+value) >= 100:
        progressiveBar.setValue(100)
    else:
        progressiveBar.setValue(int(progressiveBar.value()+value))