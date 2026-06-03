# ConvertToHtml.py
# Example how to convert PDF to HTML.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk import *

pdfix  = GetPdfix()
if pdfix is None:
    raise RuntimeError('Pdfix initialization failed')

doc = pdfix.OpenDoc(f"{inputPath}/test.pdf", "")
if doc is None:
    raise RuntimeError(f'Unable to open PDF: {pdfix.GetError()}')

htmlConv = doc.CreateHtmlConversion()
if htmlConv is None:
    raise RuntimeError(f'Unable to create HTML conversion: {pdfix.GetError()}')   

# convert all pages at once
htmlParams=PdfHtmlParams()
htmlParams.flags = kHtmlNoExternalCSS | kHtmlNoExternalJS | kHtmlNoExternalIMG
if not htmlConv.SetParams(htmlParams):
    raise RuntimeError(f'Unable to set HTML conversion parameters: {pdfix.GetError()}')    
if not htmlConv.Save(f"{outputPath}/index.html"):
    raise RuntimeError(f'Unable to save HTML document: {pdfix.GetError()}')    
    
htmlConv.Destroy()
doc.Close()