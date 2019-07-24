from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

#converts pdf, returns its text content as a string
# Alternative command
#


def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        try:
            interpreter.process_page(page)
        except Exception as e:
            print(e)
            continue
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            print("converting: " + pdf)
            pdfFilename = pdfDir + "\\" + pdf
            try:
                text = convert(pdfFilename) #get string of text content of pdf
            except Exception as e:
                print(e)
                continue
            textFilename = txtDir + "\\" + pdf + ".txt"
            print("writing to: " + textFilename)
            textFile = open(textFilename, "w") #make text file
            textFile.write(text) #write text to text file


pdfDir = r"F:\Development\pdf_downloader\combined"
txtDir = r"F:\Development\pdf_downloader\combined_txt"
convertMultiple(pdfDir, txtDir)





