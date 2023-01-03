from PdfController import PdfController
from BatchPdfController import BatchPdfController

class EntryPoint(): 
    def __init__(self,path,batch) -> None:
       
        if not batch:
            try:
                converter =  PdfController(path)
            except OSError as error:
                print(error)
                exit()
            converter.convert()
        else:
            batchController = BatchPdfController(path)
            batchController.convert()
