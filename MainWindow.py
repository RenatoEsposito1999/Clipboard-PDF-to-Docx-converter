from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from EntryPoint import EntryPoint
import sys


class MainWindow(QWidget):
    __path = None
    __progressBar = None
    __isFolder = False
    __components = []

    def __init__(self):
        app = QApplication(sys.argv)
        super(MainWindow,self).__init__()
        self.setWindowTitle("University Tool Helper")
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.setWindowIcon(QtGui.QIcon("./img/logo.jpg"))
        layout = QGridLayout()
        #Add all the components of UI
        self.__addComponent(layout)
        self.setLayout(layout)
        self.show()
        sys.exit(app.exec())

    def __addComponent(self, layout):
        self.__setFolderBox()
        self.__setPathButton()
        self.__setConvertButton()
        self.__setProgressiveBar()

        for UIobj in self.__components:
            layout.addWidget(UIobj)


    def __setProgressiveBar(self):
        #Progress bar
        self.__progressBar = QProgressBar(self)
        self.__progressBar.setValue(0)
        self.__components.append(self.__progressBar)
        #I Create a thread to handle the updating

    def __setConvertButton(self):
        #Start Button
        convertButton = QPushButton("Convert")
        convertButton.clicked.connect(self.__start)
        self.__components.append(convertButton)

    def __setFolderBox(self):
        #Add checkbox(is folder or single file)
        IsFolderBox = QCheckBox("Convert an entire folder of pdf",self)
        IsFolderBox.stateChanged.connect(self.__changeComponent)
        self.__components.append(IsFolderBox)
    
    def __setPathButton(self):
        #Add push button
        pathButton = QPushButton("Indicate the path of the file")
        pathButton.clicked.connect(self.__getPath)
        self.__components.append(pathButton)


    # Function to load Path 
    def __getPath(self):
        path = QFileDialog.getOpenFileName(self,'Indicate the path of the file/folder')
        self.__path = path[0]

    #cambiare componenti quando il checkbox è fleggato
    def __changeComponent(self):
        self.__isFolder = False if self.__isFolder else True
        


    def __start(self):
        self.__disablingButton()
        self.__progressBar.setValue(25)
        self.__progressBar.setFormat("Conversion in progress")
        self.__progressBar.setAlignment(Qt.AlignCenter)
        EntryPoint(path=self.__path, batch=self.__isFolder)
        self.__progressBar.setValue(100)
        self.__progressBar.setFormat("Conversion completed")
        self.__ConversionCompleted()

    def __ConversionCompleted(self):
        msg = QMessageBox()
        msg.setText("Conversion completed")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.__restoreState)
        x=msg.exec_()

    def __restoreState(self):
        self.__path = ""
        self.__progressBar.setValue(0)
        self.__enablingButton()
    def __disablingButton(self):
        for comp in self.__components:
            comp.setEnabled(False)
    def __enablingButton(self):
        for comp in self.__components:
            comp.setEnabled(True)


        