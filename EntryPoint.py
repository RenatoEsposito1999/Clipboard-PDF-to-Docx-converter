from PdfController import PdfController
from BatchPdfController import BatchPdfController

class EntryPoint(): 
    def __init__(self,path,batch,cleanAnnots) -> None:
       
        if not batch:
            try:
                converter =  PdfController(path)
            except OSError as error:
                print(error)
                exit()
            converter.convert(cleanAnnot=cleanAnnots)
        else:
            batchController = BatchPdfController(path)
            batchController.convert(cleanAnnot=cleanAnnots)
