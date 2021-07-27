# ConvertToHtmlByPages.py
# Example how to convert PDF to HTML.

# import utils to load required shared libraries
import ctypes
from Utils import inputPath, outputPath
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

htmlParams=PdfHtmlParams()
htmlParams.flags = kHtmlNoExternalCSS | kHtmlNoExternalJS | kHtmlNoExternalIMG| kHtmlNoExternalFONT
#htmlParams.type = kPdfHtmlResponsive
#htmlParams.image_params.format = kImageFormatJpg
#htmlParams.image_params.quality = 80

# prepare output stream
docStm = pdfix.CreateFileStream(outputPath + "/pages" +  ".html", kPsTruncate)
if not docStm:
    raise Exception('Unable to create html file : ' + pdfix.GetError())

first = bytes("<html>\n<head>\n<title>PDFix sample</title>\n</head>\n<body>\n<script>\n",encoding='ascii')
raw_first = (ctypes.c_ubyte * len(first)).from_buffer_copy(first)
docStm.Write(0, raw_first, len(raw_first))

pdfToHtml.SaveJavaScript(docStm)

sec = bytes("\n</script>\n<style>\n",encoding='ascii')
raw_sec = (ctypes.c_ubyte * len(sec)).from_buffer_copy(sec)
docStm.Write(docStm.GetSize(), raw_sec, len(raw_sec))

pdfToHtml.SaveCSS(docStm)

third = bytes("\n</style>\n",encoding='ascii')
raw_third = (ctypes.c_ubyte * len(third)).from_buffer_copy(third)
docStm.Write(docStm.GetSize(), raw_third, len(raw_third))

# convert pages
for i in range(0, doc.GetNumPages()):
    if not htmlDoc.SavePageHtml(docStm, htmlParams, i, 0, None):
        raise Exception('Unable to open html doc : ' + pdfix.GetError())

last = bytes("</body>\n</html>",encoding='ascii')
raw_last = (ctypes.c_ubyte * len(last)).from_buffer_copy(last)
docStm.Write(docStm.GetSize(), raw_last, len(raw_last))

docStm.Destroy()    
htmlDoc.Close()
doc.Close()
pdfToHtml.Destroy()
pdfix.Destroy()