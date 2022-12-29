from PdfController import PdfController
from BatchPdfController import BatchPdfController
import os
import sys
if __name__ == '__main__':
    batch = True
    if not batch:
        #app = QtWidgets.QApplication(sys.argv)
        #w = UI()
        try:
            converter =  PdfController('./PDF/Lezione 3.pdf')
        except OSError as error:
            print(error)
            exit()
        converter.convert()
        #app.exec()
    else:
        batchController = BatchPdfController('./PDF/')
        batchController.convert()