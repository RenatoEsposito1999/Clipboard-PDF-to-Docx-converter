from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui,QtWidgets
from EntryPoint import EntryPoint
import sys


class MainWindow(QWidget):
    __path = None
    __progressBar = None
    __isFolder = False
    __components = []
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Path selection")
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.setWindowIcon(QtGui.QIcon("./img/logo.jpg"))
        layout = QGridLayout()
        #Add all the components of UI
        self.__addComponent(layout)
        self.setLayout(layout)
        self.show()
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
        path = QFileDialog.getOpenFileName(self,'Indicate the path of the file')
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


def getOpenFilesAndDirs(parent=None, caption='', directory='', 
                        filter='', initialFilter='', options=None):
    def updateText():
        # update the contents of the line edit widget with the selected files
        selected = []
        for index in view.selectionModel().selectedRows():
            selected.append('"{}"'.format(index.data()))
        lineEdit.setText(' '.join(selected))

    dialog = QtWidgets.QFileDialog(parent, windowTitle=caption)
    dialog.setFileMode(dialog.ExistingFiles)
    if options:
        dialog.setOptions(options)
    dialog.setOption(dialog.DontUseNativeDialog, True)
    if directory:
        dialog.setDirectory(directory)
    if filter:
        dialog.setNameFilter(filter)
        if initialFilter:
            dialog.selectNameFilter(initialFilter)

    # by default, if a directory is opened in file listing mode, 
    # QFileDialog.accept() shows the contents of that directory, but we 
    # need to be able to "open" directories as we can do with files, so we 
    # just override accept() with the default QDialog implementation which 
    # will just return exec_()
    dialog.accept = lambda: QtWidgets.QDialog.accept(dialog)

    # there are many item views in a non-native dialog, but the ones displaying 
    # the actual contents are created inside a QStackedWidget; they are a 
    # QTreeView and a QListView, and the tree is only used when the 
    # viewMode is set to QFileDialog.Details, which is not this case
    stackedWidget = dialog.findChild(QtWidgets.QStackedWidget)
    view = stackedWidget.findChild(QtWidgets.QListView)
    view.selectionModel().selectionChanged.connect(updateText)

    lineEdit = dialog.findChild(QtWidgets.QLineEdit)
    # clear the line edit contents whenever the current directory changes
    dialog.directoryEntered.connect(lambda: lineEdit.setText(''))

    dialog.exec_()
    return dialog.selectedFiles()