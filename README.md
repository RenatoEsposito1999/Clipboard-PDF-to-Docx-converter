# PDF TO WORD CONVERTER
##### Table of Contents
- [Premises](#Premises)
- [Overview](#overview)  
- [Instructions](#instructions)
  - [Requirements](#requirements-(by-downloading-the-source-code))
  - [Requirements](#Requirements-(by-downloading-the-.exe))
  - [Interface explanation](#interface-explanation)
  - [How to install all the necessary libraries](#how-to-install-all-the-necessary-libraries)
- [License](#license)
- [Contacts](#contacts) 

## Premises
[UPDATE 2024] This project was developed rapidly, based on my skills and knowledge at the time. It's important to note that during development, I may not have strictly adhered to commonly accepted architectural patterns such as the Model-View-Controller (MVC) pattern.

The primary purpose of this project was to create a study support tool for university exams, with the aim of facilitating my own learning process and that of my peers. Therefore, the main focus was on implementing the necessary features to achieve this specific goal, rather than rigidly adhering to more complex design conventions.

After a year of continuous use, I can confirm that this tool has fully achieved its sole creation objective. It has proven to be a valuable ally in studying, providing practical support throughout the academic journey.

I hope that this project can be equally useful for other students in similar situations, providing them with an additional option to enhance the efficiency and effectiveness of their learning process.

## Overview
***
The goal of this software is to convert pdf files into docx files where:

 - Notes on the pdf (taken with normal software such as Adobe Acrobat,
   Edge etc.) are converted into editable text in word. 
- The pdf page becomes an image in word.

The final result is then an editable docx file where for each page of the pdf there will be a docx page with the annotations in text format and a screenshot of the pdf page they were on.
The image below shows just the final result.


For example given the following pdf in input
<p align="center">
<img src="https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/blob/main/Resources/pdf%20input.png" width="500" height="500">
</p>

We get the following docx as output

<p align="center"><img src="https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/blob/main/Resources/docx%20output.png" width="500" height="500"></p>

**N.B**: It's possible through an option within the software to clean the images by eliminating the annotations before taking the screenshot, in this case we get the following output:
<p align="center"><img src="https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/blob/main/Resources/docxoutputwithoutannots.png" width="500" height="500"></p>


## Instructions
***
### Requirements (by downloading the source code)
- [The source code](https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/releases/tag/PDF-to-Docx-converter-v1)
- [Python > 3.9](https://www.python.org/downloads/)
- [The necessary libraries](#how-to-install-all-the-necessary-libraries)
- [Visual Studio or any other editor](https://visualstudio.microsoft.com/it/downloads/)
- [(Optional) GitHub Desktop](https://desktop.github.com/)

### Requirements (by downloading the .exe)
- [.exe](https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/releases/tag/PDF-to-Docx-converter-v1)


### Interface explanation
**Brief preamble**


The graphical interface has not been treated in detail due to lack of time, it is minimalistic with few and simple instructions.
Anyone who wants to update the graphical interface is welcome, all they have to do is work on the [MainWindow.py](https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/blob/main/MainWindow.py) class

<p align="center"><img algin="right" src="https://github.com/RenatoEsposito1999/PDF-to-Docx-converter-with-annotations/blob/main/Resources/gui.png" width="300" height="300"></p>


- **The first checkbox**: if checked it will be possible to select an entire folder. This will be inspected and will convert all pdf's inside.
- **The first checkbox**: if checked it will delete the clipboard from the pdf page before taking the screenshot. (**WARNING: this option will not modify the original pdf in any way so the notes will continue to be there at the end of the process**)
- **The third element**: allows you to select the pdf/folder containing the pdfs.
- **The fourth element**: start the conversion process. (**WARNING**: if the file extension is not pdf the process will do nothing)
- **The last element**: is a bar that indicates the progress of the process.


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
