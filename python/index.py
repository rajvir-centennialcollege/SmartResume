# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:41:07 2019

@author: Duggal
"""

import tabula

def Main():
    df = tabula.read_pdf("Sample/sample.pdf")
    print(df)

if __name__ == '__main__':
    Main()