import fitz
from fitz import Annot
#Valutare di usare fitz per gestire i PDF. Fitz dovrebbe contenere PyMuPDF.
class PDF:
    #The pdf file reader
    _doc = None
    def __init__(self,path):
        _doc = fitz.open(path)
        #For each page of the pdf
        for page in _doc:
            for annot in page.annots():
                #print(annot.get_textbox(Annot.rect))
                print(page.clean_contents())
                #print(f"La nota eliminata e'. {page.delete_annot(annot)}")
        _doc.save('UpdatedPDF.pdf')
        i = 0
        '''
        Riesco a ricavare le foto delle pagine.
        for page in _doc:
            pix = page.get_pixmap()  # render page to an image
            #pix.save(f"page_{i}.png")
            i+=1
        exit()
        '''

'''
SITUAZIONE ATTUALE:
Allora stato attuale riesco a prendere la nota e ad eliminarla, ma elimino anhe i disegni e non vorrei farlo
COSE DA FARE:
- Modificare il size delle foto da codice (in futoro sarà un parametro dell'app)
- Trovare un modo per ripulire prima le foto dalle note e solo dopo scattare la foto della slide, ovviamente le note non devono andare perse.
- Mettere il tutto in ordine su un file word.
- Comprimere le immagini
- Rendere come parametri di input sia il size delle foto che la scelta di cancellare gli appunti dalle foto, quindi prima di fare la foto si cancellano gli appunti
chiaramente non si salverà il PDF qvecchio quindi non li perdono dalla versione del vecchio. 
'''