from PyPDF2 import PdfFileReader
import fitz 
#Valutare di usare fitz per gestire i PDF. Fitz dovrebbe contenere PyMuPDF.
class PDF:
    #The pdf file reader
    _parser = None
    def __init__(self,path):
        _parser = PdfFileReader(path)
        #For each page of the pdf
        for page in _parser.pages:
            try:
                for annot in page["/Annots"]:
                    print(annot.getObject()['/Contents'])
            except:
                pass        

        doc = fitz.open(path)  # open document
        i = 0
        for page in doc:
            pix = page.get_pixmap()  # render page to an image
            pix.save(f"page_{i}.png")
            i+=1
        exit()


'''
SITUAZIONE ATTUALE:
Riesco a etrarre le note dalle pagine e riesco a ricavare le foto delle pagine.
COSE DA FARE:
- Modificare il size delle foto da codice (in futoro sarà un parametro dell'app)
- Usare PyMuPDF al posto di PyPDF2 per ottenere le annotazioni.
- Numerare le foto in base all'indice che va da 0 al numero della foto. 
- Trovare un modo per ripulire prima le foto dalle note e solo dopo scattare la foto della slide, ovviamente le note non devono andare perse.
- Mettere il tutto in ordine su un file word.
'''