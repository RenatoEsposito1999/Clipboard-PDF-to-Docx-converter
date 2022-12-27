import fitz
from DocxController import DocxController
import os
class PdfController:
    #The pdf file reader
    __PDFdoc = None
    __DocxController = None
    __orig_doc = None
    __path = None
    def __init__(self,path):
        if (not path.lower().endswith('.pdf')) or (not os.path.exists(path)):
            raise Exception("Non-existent file or wrong extension")
        self.__orig_doc =  fitz.open(path)
        self.__PDFdoc = fitz.Document()
        #I work with one copy to avoid breakage
        self.__PDFdoc.insert_pdf(self.__orig_doc)
        self.__DocxController = DocxController(self.__orig_doc.name)

    def __scan(self,cleanAnnot = False):
        for page in self.__PDFdoc: #For each page of the pdf
            for annot in page.annots():
                if annot.info['content']: #content is not null when has text
                    self.__InsertText(annot.info['content'])
                    if cleanAnnot: #User wants to delete notes on images in docx 
                        page.delete_annot(annot)
            self.__InsertPhoto(page) 

    #CleanAnnot = false converter don't clear the annotations.
    def convert(self, cleanAnnot = False):
        self.__scan(cleanAnnot)             
        self.__closeDoc()

    def __InsertText(self,txt):
        self.__DocxController.InsertText(txt)

    def __InsertPhoto(self,page):
        pix = page.get_pixmap()
        name = f"page_{page.number}.png"
        pix.save(name)
        self.__DocxController.InsertPhoto(name)

#optional parameters are required for the case where it is not batch
    def __closeDoc(self,batch = False, folder = None):
        self.__PDFdoc.close()
        self.__orig_doc.close()
        self.__DocxController.Save(batch,folder)

        
        
                


