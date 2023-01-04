# PDF TO WORD CONVERTER
## Overview
***
The goal of this software is to convert pdf files into docx files where:

 - Notes on the pdf (taken with normal software such as Adobe Acrobat,
   Edge etc.) are converted into editable text in word. 
- The pdf page becomes an image in word.

The final result is then an editable docx file where for each page of the pdf there will be a docx page with the annotations in text format and a screenshot of the pdf page they were on.
The image below shows just the final result.


For example given the following pdf in input

<img src="https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/blob/main/Resources/pdf%20input.png" width="500" height="500">


We get the following docx as output


<img src="https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/blob/main/Resources/docx%20output.png" width="500" height="500">

**N.B**: It's possible through an option within the software to clean the images by eliminating the annotations before taking the screenshot, in this case we get the following output:

<img src="https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/blob/main/Resources/docxoutputwithoutannots.png" width="500" height="500">


## Instructions
***
### Requirements (by downloading the source code)
- [Python > 3.9](https://www.python.org/downloads/)
- [The necessary libraries](#How to install all the necessary libraries)
- [Visual Studio or any other editor](https://visualstudio.microsoft.com/it/downloads/)
- [(Optional) GitHub Desktop](https://desktop.github.com/)

### Requirements (by downloading the .exe)
...

### Interface explanation


**Brief preamble**


The graphical interface has not been treated in detail due to lack of time, it is minimalistic with few and simple instructions.
Anyone who wants to update the graphical interface is welcome, all they have to do is work on the [MainWindow.py](https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/blob/main/MainWindow.py) class

### How to install all the necessary libraries
In order to do this, it is necessary to go from the terminal to the "PDF-to-Docx-converter-with-annotations" folder and type the command:

    pip install -r requirements.txt
**pip** will take care of doing all the work.

## License ☢️
***
PDF-to-Docx-converter-with-annotations is licensed under the GNU General Public License v3.0. Please, see the 
[license](https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/blob/main/LICENSE).

## Contacts 🪪
***
- [mail] renato [ dot ] esposito1999 [ at ] outlook [ dot ] com (you can write to me in english or italian).


**04/01/2023**
