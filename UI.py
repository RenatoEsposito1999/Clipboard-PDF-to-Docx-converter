import sys
from PDF import PDF
'''
    Sistemare il layout della UI, capire bene come funziona la gerarchia e come conviene 
    operare in PyQT5.
    Probabilment devo aggiungere un widget a main window e modificare quello, leggere
    https://stackoverflow.com/questions/60626627/pyqt5-how-to-get-the-mainwindow-layout
    utente pavan chandaka.

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        self.setWindowTitle('PDF TO WORD CONVERTER')

        #BROWSER BUTTON
        button = QPushButton('Browse',self)
        button.clicked.connect(self.browsefiles)
        self.show()
        
    def browsefiles(self):
        path = QFileDialog.getOpenFileName(self,'APRI')
        PDF(path[0])
'''
if __name__ == '__main__':
    #app = QtWidgets.QApplication(sys.argv)
    #w = UI()
    PDF('./Presentation1.pdf')
    #app.exec()
