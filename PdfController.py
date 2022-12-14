import fitz
from DocxController import DocxController
class PdfController:
    #The pdf file reader
    __PDFdoc = None
    __DocxController = None
    def __init__(self,path):
        _orig_doc =  fitz.open(path)
        self.__PDFdoc = fitz.Document()
        #I work with one copy to avoid breakage
        self.__PDFdoc.insert_pdf(_orig_doc)
        self.__DocxController = DocxController(_orig_doc.name)
        _orig_doc.close()



    def convert(self):
        for page in self.__PDFdoc: #For each page of the pdf
            for annot in page.annots():
                if annot.info['content']: #content is not null when has text
                    #self.__addTxtDocx(annot.info['content'])
                    #page.delete_annot(annot)
                    print(annot.info['content'])
                else: #if content has null value is a drawing
                    print("la stringa è vuota")
        i = 0
        
        self.__closeDoc()
        '''
        Riesco a ricavare le foto delle pagine.
        for page in _doc:
            pix = page.get_pixmap()  # render page to an image
            #pix.save(f"page_{i}.png")
            i+=1
        exit()
        '''

    def __closeDoc(self):
        self.__PDFdoc.close()
        self.__DocxController.save()
        
        

'''
SITUAZIONE ATTUALE:
Allora stato attuale riesco a differenziare i disegni dalle annotazioni scritte. Ora devo caricarli sul file word
COSE DA FARE:
- Modificare il size delle foto da codice (in futuro sarà un parametro dell'app)
- Trovare un modo per ripulire prima le foto dalle note e solo dopo scattare la foto della slide, ovviamente le note non devono andare perse.
- Mettere il tutto in ordine su un file word.
- Comprimere le immagini
- Rendere come parametri di input sia il size delle foto che la scelta di cancellare gli appunti dalle foto, quindi prima di fare la foto si cancellano gli appunti
chiaramente non si salverà il PDF qvecchio quindi non li perdono dalla versione del vecchio. 
- Verificare che il documento sia un .pdf e gestire l'errore di file broken.
- Verificare sempre che il save porta a file non duplicati altrimenti potrebbero esserci dei problemi di sovrascrittura.
'''