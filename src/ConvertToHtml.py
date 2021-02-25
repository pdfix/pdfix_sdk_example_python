# ConvertToHtml.py
# Example how to convert PDF to HTML.

# import initialization to load required shared libraries
from Initialization import inputPath, outputPath
from Pdfix import *
from PdfToHtml import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

# initialize pdf to html plugin
pdfToHtml = GetPdfToHtml()
if pdfToHtml is None:
    raise Exception('PdfToHtml Initialization fail')
if not pdfToHtml.Initialize(pdfix):
    raise Exception('PdfToHtml Initialize Pdfix fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

htmlDoc = pdfToHtml.OpenHtmlDoc(doc)
if htmlDoc is None:
    raise Exception('Unable to open html doc : ' + pdfix.GetError())   

# convert all pages at once
htmlParams=PdfHtmlParams()
htmlParams.flags = kHtmlNoExternalCSS | kHtmlNoExternalJS | kHtmlNoExternalIMG
if not htmlDoc.Save(outputPath + "/index.html", htmlParams, 0, None):
    raise Exception('Unable to open html doc : ' + pdfix.GetError())    
    
doc.Close()
