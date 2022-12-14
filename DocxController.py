from docx import Document
import re

class DocxController:
    __doc = None
    __title = None
    def __init__(self,title):
        self.__doc = Document()
        self.__title = re.sub(".pdf",".docx",title)

#CONTROLLARE SE GIA' ESISTE. 
    def save(self):
        print(self.__title)
        self.__doc.save(self.__title)

