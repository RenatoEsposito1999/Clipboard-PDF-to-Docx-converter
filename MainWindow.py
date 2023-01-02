from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from EntryPoint import EntryPoint
import sys

class MainWindow(QMainWindow):
    __path = None
    __isFolder = False
    __components =[]
    def __init__(self):

        app = QApplication(sys.argv)
        super(MainWindow,self).__init__()
        self.setWindowTitle("University Tool Helper")
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        widgets = QWidget()
        #layout = QGridLayout()
        # Add all the components of UI
        self.__addComponent(widgets)
        #widgets.setLayout(layout)
        mainWidgets = QStackedWidget(widgets)
        self.setCentralWidget(mainWidgets)
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
        progressBar = QProgressBar(self)
        self.__components.append(progressBar)

    def __setConvertButton(self):
        #Start Button
        convertButton = QPushButton("Convert")
        convertButton.clicked.connect(self.__start)
        self.__components.append(convertButton)

    def __setFolderBox(self):
        #Add checkbox(is folder or single file)
        IsFolderBox = QCheckBox("check if you want convert an entire folder of pdf",self)
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

    def __changeComponent(self):
        self.__isFolder = False if self.__isFolder else True
        print(self.__isFolder)


    def __start(self):
        EntryPoint(path=self.__path, batch=self.__isFolder)

    def __updateBar(self,progressBar):
        i = 0
        while True:
            i+=0.1
            progressBar.setValue(i)

