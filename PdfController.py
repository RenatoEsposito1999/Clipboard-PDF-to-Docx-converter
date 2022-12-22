import fitz
from DocxController import DocxController
class PdfController:
    #The pdf file reader
    __PDFdoc = None
    __DocxController = None
    __orig_doc = None
    def __init__(self,path):
        self.__orig_doc =  fitz.open(path)
        self.__PDFdoc = fitz.Document()
        #I work with one copy to avoid breakage
        self.__PDFdoc.insert_pdf(self.__orig_doc)
        self.__DocxController = DocxController(self.__orig_doc.name)



    def convert(self, cleanAnnot = True):
        for page in self.__PDFdoc: #For each page of the pdf
            for annot in page.annots():
                if annot.info['content']: #content is not null when has text
                    self.__InsertText(annot.info['content'])
                    if cleanAnnot: #User wants to delete notes on images in docx 
                        page.delete_annot(annot)
            self.__InsertPhoto(page)                
        self.__closeDoc()

    def __InsertText(self,txt):
        self.__DocxController.InsertText(txt)

    def __InsertPhoto(self,page):
        pix = page.get_pixmap()
        name = f"page_{page.number}.png"
        pix.save(name)
        self.__DocxController.InsertPhoto(name)

    def __closeDoc(self):
        self.__PDFdoc.close()
        self.__orig_doc.close()
        self.__DocxController.Save()
        
        

'''
SITUAZIONE ATTUALE:
Allora stato attuale riesco a differenziare i disegni dalle annotazioni scritte. Ora devo caricarli sul file word
COSE DA FARE:
- Modificare il size delle foto da codice (in futuro sarà un parametro dell'app)
- Rendere come parametri di input sia il size delle foto che la scelta di cancellare gli appunti dalle foto, quindi prima di fare la foto si cancellano gli appunti
chiaramente non si salverà il PDF qvecchio quindi non li perdono dalla versione del vecchio. 
- Verificare che il documento sia un .pdf
- Verificare sempre che il save porta a file non duplicati altrimenti potrebbero esserci dei problemi di sovrascrittura.
'''