import fitz 
#Valutare di usare fitz per gestire i PDF. Fitz dovrebbe contenere PyMuPDF.
class PDF:
    #The pdf file reader
    _doc = None
    def __init__(self,path):
        _doc = fitz.open(path)
        #For each page of the pdf
        for page in _doc:
            for annot in page.annots():
                print(annot.get_text())        
        i = 0
        for page in _doc:
            pix = page.get_pixmap()  # render page to an image
            #pix.save(f"page_{i}.png")
            i+=1
        exit()


'''
SITUAZIONE ATTUALE:
Riesco a ricavare le foto delle pagine.
COSE DA FARE:
- Estrarre il testo dalle annotazioni, credo che devo lavorare su annot ma ci sono anche altre cose:
leggi : https://pymupdf.readthedocs.io/en/latest/tutorial.html WORKING WITH PAGE
- Modificare il size delle foto da codice (in futoro sarà un parametro dell'app)
- Usare PyMuPDF al posto di PyPDF2 per ottenere le annotazioni.
- Numerare le foto in base all'indice che va da 0 al numero della foto. 
- Trovare un modo per ripulire prima le foto dalle note e solo dopo scattare la foto della slide, ovviamente le note non devono andare perse.
- Mettere il tutto in ordine su un file word.
- Comprimere le immagini
'''