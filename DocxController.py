from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
import re
import os

class DocxController:
    __doc = None
    __title = None
    def __init__(self,title):
        self.__doc = Document()
        self.__title = re.sub(".pdf",".docx",title)
        #ADD only the name (not the path) without .docx extension
        self.__doc.add_heading(os.path.basename(re.sub(".docx","",self.__title)),level = 0)
        


    def InsertText(self,text):
        p = self.__doc.add_paragraph().add_run(text)
        #CALIBRI 12
        p.font.size = Pt(13)
        p.font.name = 'Calibri'
    def InsertPhoto(self,imageName):
        self.__doc.add_picture(imageName, width = Inches(6.61), height = Inches(3.9))
        os.remove("./"+imageName)

#CONTROLLARE SE GIA' ESISTE. 
    def Save(self):
        print(self.__title)
        self.__doc.save(self.__title)
        #Verificare sempre che il save porta a file non duplicati altrimenti potrebbero esserci dei problemi di sovrascrittura.


