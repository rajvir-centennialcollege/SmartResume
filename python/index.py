# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:41:07 2019

@author: Duggal
"""

import PyPDF2
import re

class GetPDF:
    pdfPath   = ""
    pdf       = ""
    numPages  = 0
    content   = []
    links     = []
    phonenum  = []
    email     = [] 
    
    def __init__(self, pdfPath):
        self.pdfPath = pdfPath
#        -------------- READING AND SETTING VALUES
        with open(pdfPath,'rb') as pdfObj:
            pdfReader = PyPDF2.PdfFileReader(pdfObj)
            self.setNumPages(pdfReader.numPages)
            
            for i in range(self.getNumPages()):
                self.setContent(pdfReader.getPage(i).extractText())
                
            self.extractText()
       
#        ------------------ EXTRACTING TEXT FROM PDF
        
    def extractText(self):
        lines = self.content[0]
        lines = lines.split('\n')
        for i in lines:
            if len(self.FindEmail(i)) != 0:
                self.setemail(i)
            
            if len(self.FindURL(i)) != 0:
                self.setLinks(i)
                
        print(self.getemail())
        print(self.getLink())
    
#    ---------------- REGULAR EXPRESSSION FOR URL AND EMAIL
        
    def FindURL(self, string):  
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
        return url 
    
    def FindEmail(self, string):
        emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", string)
        return emails
    
#    -------------- GETTER SETTER OF CLASS
    def setNumPages(self, numPages):
        self.numPages = numPages
    
    def getNumPages(self):
        return self.numPages
    
    def setContent(self, content):
        self.content.append(content)
    
    def getContent(self):
        return self.content
    
    def setLinks(self, link):
        self.links.append(link)
    
    def getLink(self):
        return self.links
    
    def setemail(self, email):
        self.email.append(email)
    
    def getemail(self):
        return self.email

def Main():
    pdfPath = "Sample/sample4.pdf"
     
    pdfObj = GetPDF(pdfPath)

    
if __name__ == '__main__':
    Main()