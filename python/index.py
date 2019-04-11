# -*- coding: utf-8 -*-a
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
    content   = set()
    links     = set()
    phonenum  = set()
    email     = set()
    
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
        for i in range(len(self.content)):   
            lines = list(self.content)[i]
            lines = lines.split('\n')
            for i in lines:
#                print(">>>> " + i)
                if len(self.FindEmail(i)) != 0:
                    self.setemail(i)
                
                if len(self.FindURL(i)) != 0:
                    print("=> " + i)
                    self.setLinks(i)
                    
        print(self.getemail())
        print(self.getLink())
    
#    ---------------- REGULAR EXPRESSSION FOR URL AND EMAIL
        
    def FindURL(self, string):  
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
#        url = re.findall("[-a-zA-Z0-9@:%.\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%\+.~#?&//=]*)", string) 
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
        self.content.add(content)
    
    def getContent(self):
        return self.content
    
    def setLinks(self, link):
        self.links.add(link)
    
    def getLink(self):
        return self.links
    
    def setemail(self, email):
        self.email.add(email.strip())
    
    def getemail(self):
        return self.email

def Main():
    pdfPath = "Sample/sample3.pdf"
     
#    a = set()
#    a.add(2)
#    a.add(5)
#    a.add(2)
#    print(list(a)[0])
    
    pdfObj = GetPDF(pdfPath)

    
if __name__ == '__main__':
    Main()