# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:41:07 2019

@author: Duggal
"""

import PyPDF2

def Main():
    pdfFile   = open('Sample/sample.pdf', 'rb')
    
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    print("Number of Pages : " + str(pdfReader.numPages))
    
    for pagesInfo in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pagesInfo)
        print(">>>>> " + pageObj.extractText())
    
    pdfFile.close()
    
if __name__ == '__main__':
    Main()