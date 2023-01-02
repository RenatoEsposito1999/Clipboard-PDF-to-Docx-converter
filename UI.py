from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from EntryPoint import EntryPoint
import sys

class UI(QWidget):
    __path = None
    __isFolder = False
    def __init__(self):
        app = QApplication(sys.argv)
        super(UI,self).__init__()
        self.setWindowTitle("University Tool Helper")
        
        layout = QGridLayout()
        # Add all the components of UI
        self.__addComponent(layout)
        self.setLayout(layout)
        self.show()
        sys.exit(app.exec())

    def __addComponent(self, layout):
        #Add checkbox(is folder or single file)
        IsFolderBox = QCheckBox("check if you want convert an entire folder of pdf",self)
        IsFolderBox.stateChanged.connect(self.__changeComponent)
        layout.addWidget(IsFolderBox)
        #Add push button
        pathButton = QPushButton("Indicate the path of the file")
        pathButton.clicked.connect(self.__getPath)
        layout.addWidget(pathButton)

        startButton = QPushButton("Start")
        startButton.clicked.connect(self.__start)

        layout.addWidget(startButton)



    # Function to load Path 
    def __getPath(self):
        path = QFileDialog.getOpenFileName(self,'Indicate the path of the file/folder')
        self.__path = path[0]


    def __changeComponent(self):
        self.__isFolder = False if self.__isFolder else True
        print(self.__isFolder)


    def __start(self):
        EntryPoint(path=self.__path, batch=self.__isFolder)
