from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from EntryPoint import EntryPoint
#from progressBarController import * 
import ProgressBarController
class MainWindow(QWidget):
    __path = None
    __isFolder = False
    __browse = None
    __IsFolderBox = None
    __clearAnnots = False
    __components = []
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("PDF to Docx converter with annotations")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        layout = QGridLayout()
        #Add all the components of UI
        self.__addComponent(layout)
        self.setLayout( layout)
        self.show()
    def __addComponent(self, layout):
        self.__setFolderBox()
        self.___setClearAnnots()
        self.__setPathButton()
        self.__setConvertButton()
        self.__setProgressiveBar()
        

        for UIobj in self.__components:
            layout.addWidget(UIobj)

    def ___setClearAnnots(self):
        #Check Box for clear annotations
        checkbox = QCheckBox("Clean up pdf annotations on word images \n(This action will not touch\n the original pdf in any way)",self)
        checkbox.clicked.connect(self.__changeClearAnnots)
        self.__components.append(checkbox)


    def __changeClearAnnots(self):
        self.__clearAnnots = False if self.__clearAnnots else True


    def __setProgressiveBar(self):
        #Progress bar
        self.__components.append(ProgressBarController.initBar())
        #I Create a thread to handle the updating

    def __setConvertButton(self):
        #Start Button
        convertButton = QPushButton("Convert")
        convertButton.setFixedSize(QtCore.QSize(230, 30))
        convertButton.clicked.connect(self.__start)
        self.__components.append(convertButton)

    def __setFolderBox(self):
        #Add checkbox(is folder or single file)
        self.__IsFolderBox = QCheckBox("Convert an entire path",self)
        self.__IsFolderBox.stateChanged.connect(self.__changeComponent)
        self.__components.append(self.__IsFolderBox)
    
    def __setPathButton(self):
        #Add push button
        self.__browse = QPushButton("Indicate the path of the file")
        self.__browse.clicked.connect(self.__getPath)

        self.__browse.setFixedSize(QtCore.QSize(230, 30))
        self.__components.append(self.__browse)


    # Function to load Path 
    def __getPath(self):

        if not self.__isFolder:
            path = QFileDialog.getOpenFileName(self,'Indicate the path of the file')
            if not self.__path:
                self.__path = path[0]
        else:
            path = str(QFileDialog.getExistingDirectory(self, "Indicate the folder's path"))
            if not self.__path:
                self.__path = path
    def __changeComponent(self):
        #TRUE
        if self.__isFolder:
            self.__isFolder = False
            self.__browse.setText("Indicate the path of the file")
            self.__IsFolderBox.setText("Convert an entire path")
        #FALSE
        else:
            self.__isFolder = True
            self.__browse.setText("Indicate the folder's path")

    def __start(self):
        if  self.__path == None or self.__path == "":
            self.__customError("Undefined path")
        else:
            self.__disablingButton()
            EntryPoint(path=self.__path, batch=self.__isFolder,cleanAnnots=self.__clearAnnots)
            ProgressBarController.updateValue(50)
            self.__ConversionCompleted()
            
    
    def __customError(self,txt):
        msg = QMessageBox()
        msg.setText(txt)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.__restoreState)
        x=msg.exec_()

    def __ConversionCompleted(self):
        msg = QMessageBox()
        msg.setWindowTitle("Conversion completed")
        msg.setText("Conversion completed")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.__restoreState)
        x=msg.exec_()

    def __restoreState(self):
        self.__path = None
        ProgressBarController.clearProgress()
        self.__enablingButton()
    def __disablingButton(self):
        for comp in self.__components:
            comp.setEnabled(False)
    def __enablingButton(self):
        for comp in self.__components:
            comp.setEnabled(True)

