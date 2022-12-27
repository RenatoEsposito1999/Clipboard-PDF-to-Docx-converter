from PdfController import PdfController
from BatchPdfController import BatchPdfController
import os
if __name__ == '__main__':
    batch = True
    if not batch:
        #app = QtWidgets.QApplication(sys.argv)
        #w = UI()
        try:
            converter =  PdfController('./PDF/Lezione 3.pdf')
        except:
            print("Non-existent file or wrong extension\n")
            exit()
        converter.convert()
        #app.exec()
    else:
        batchController = BatchPdfController('./PDF/')