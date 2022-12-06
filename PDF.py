from PyPDF2 import PdfFileReader
class PDF:
    #The pdf file reader
    _parser = None
    def __init__(self,path):
        _parser = PdfFileReader(path)
        index = 0
        #For each page of the pdf
        for page in _parser.pages:
            '''
            _parser._get_page(index).extract_text()
            index+=1
            '''
            try:
                for annot in page["/Annots"]:
                    print(annot.getObject()['/Contents'])
            except:
                pass        
        exit()