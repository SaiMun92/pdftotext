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
    if pdfDir == "":
        pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
    for root, dirs, files in os.walk(pdfDir):
        for pdf in files:
            fileExtension = pdf.split(".")[-1]
            filename = pdf.split(".")[0]
            if fileExtension == "pdf":
                print("converting: " + pdf)
                pdfFilename = os.path.join(root, pdf)
                try:
                    text = convert(pdfFilename) #get string of text content of pdf
                except Exception as e:
                    print(e)
                    continue
                # textFilename = txtDir + "\\" + pdf + ".txt"
                outroot = root.replace(pdfDir, txtDir)
                textFilename = os.path.join(outroot, filename) + ".txt"
                if not os.path.isdir(outroot):
                    os.makedirs(outroot)

                print("writing to: " + textFilename)
                textFile = open(textFilename, "w") #make text file
                textFile.write(text) #write text to text file


pdfDir = r"C:\Users\huangdajing\Desktop\Cases_from_ICMS_s323"
txtDir = r"C:\Users\huangdajing\Desktop\Cases_from_ICMS_s323_txt"
convertMultiple(pdfDir, txtDir)





