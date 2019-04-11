# -*- coding: utf-8 -*-a
"""
Created on Wed Apr  3 16:41:07 2019

@author: Duggal
"""

import PyPDF2
import re
import predict

class GetPDF:
    pdfPath     = ""
    pdf         = ""
    numPages    = 0
    content     = set()
    links       = set()
    phonenum    = set()
    email       = set()
    pointScored = []
    
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
#        print(predict.predict("hello"))
        for i in range(len(self.content)):
            lines = list(self.content)[i]
            lines = lines.split('\n')
            for i in lines:
                i = i.strip()
                if len(i) > 0:
                    points = predict.predict(i)
                    self.setPoints(points)
                    if len(self.FindEmail(i)) != 0:
                        self.setemail(i)
                    
                    if len(self.FindURL(i)) != 0:
    #                    print("=> " + i)
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
        self.content.add(content.strip())
    
    def getContent(self):
        return self.content
    
    def setLinks(self, link):
        self.links.add(link.strip())
    
    def getLink(self):
        return self.links
    
    def setemail(self, email):
        self.email.add(email.strip())
    
    def getemail(self):
        return self.email
    
    def setPoints(self, points):
        self.pointScored.append(points)
    
    def getPoint(self):
        return self.pointScored
    
    
def Main():
    pdfPath = "Sample/sample4.pdf"
    
    pdfObj = GetPDF(pdfPath)

    
if __name__ == '__main__':
    Main()