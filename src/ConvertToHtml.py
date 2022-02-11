# ConvertToHtml.py
# Example how to convert PDF to HTML.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

htmlConv = doc.CreateHtmlConversion()
if htmlConv is None:
    raise Exception('Unable to open html doc : ' + pdfix.GetError())   

# convert all pages at once
htmlParams=PdfHtmlParams()
htmlParams.flags = kHtmlNoExternalCSS | kHtmlNoExternalJS | kHtmlNoExternalIMG
if not htmlConv.SetParams(htmlParams):
    raise Exception('Unable to set params : ' + pdfix.GetError())    
if not htmlConv.Save(outputPath + "/index.html", 0, None):
    raise Exception('Unable to open html doc : ' + pdfix.GetError())    
    
htmlConv.Destroy()
doc.Close()