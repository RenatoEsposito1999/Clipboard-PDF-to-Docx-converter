from PdfController import PdfController
if __name__ == '__main__':
    #app = QtWidgets.QApplication(sys.argv)
    #w = UI()
    try:
        converter =  PdfController('./Lezione 3.pdf')
    except:
        print("Non-existent file or wrong extension\n")
        exit()
    converter.convert(False)
    #app.exec()