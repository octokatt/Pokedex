
# First Attempt at Scraping for the Pokedex Project

import PyPDF2

pdfFileObj = open('/Users/katt/Documents/Code/Pokedex/project/data/raw/Pokedex_1.05.pdf')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)