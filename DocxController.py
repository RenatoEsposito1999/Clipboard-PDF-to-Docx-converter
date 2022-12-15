from docx import Document
import re

class DocxController:
    __doc = None
    __title = None
    def __init__(self,title):
        self.__doc = Document()
        self.__title = re.sub(".pdf",".docx",title)

    def InsertText(self,text):
        self.__doc.add_heading(self.__title, 0)
        self.__doc.add_paragraph(text)

    def InsertPhoto(self,imageName):
        self.__doc.add_picture(imageName)


#CONTROLLARE SE GIA' ESISTE. 
    def Save(self):
        print(self.__title)
        self.__doc.save(self.__title)

