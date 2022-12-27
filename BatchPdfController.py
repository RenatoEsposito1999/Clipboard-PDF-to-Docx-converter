import os
from PdfController import PdfController
class BatchPdfController():
    __PdfController = None
    def __init__(self,path):
        for file in os.listdir(path):
            if (path+file).lower().endswith('.pdf'):
                self.__PdfController = PdfController(path+file)
                try:
                    self.__PdfController.convert(batch = True,folder=path)
                except OSError as error:
                    print("Batch: ", error)
                    exit()
