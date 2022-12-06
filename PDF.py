from PyPDF2 import PdfFileReader


class PDF:
    #PDF is the pdfFileReader
    _pdfFR = None
    def __init__(self,path):
        print(f"Path ricevuto:{path} di tipo {type(path)}")