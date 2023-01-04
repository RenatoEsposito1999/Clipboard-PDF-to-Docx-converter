import os
from PdfController import PdfController
class BatchPdfController(PdfController):
    __Batch = None
    __folder = None

    def __init__(self,path):
        self.__Batch =[]
        self.__folder = path
        for file in os.listdir(path):
            if (path+file).lower().endswith('.pdf'):
                self.__Batch.append(file)



    def convert(self, cleanAnnot=False):

        for file in self.__Batch:
            try:
                super().__init__(self.__folder+"/"+file)
            except OSError as error:
                print("Batch" + error)
            self._PdfController__scan(cleanAnnot)
            self._PdfController__closeDoc(batch=True,folder=self.__folder, nElements=len(self.__Batch))
