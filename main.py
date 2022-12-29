from PdfController import PdfController
from BatchPdfController import BatchPdfController
from UI import UI
if __name__ == '__main__':
    batch = True
    ui = UI()
    if not batch:
        try:
            converter =  PdfController('./PDF/Lezione 3.pdf')
        except OSError as error:
            print(error)
            exit()
        converter.convert()
    else:
        batchController = BatchPdfController('./PDF/')
        batchController.convert()