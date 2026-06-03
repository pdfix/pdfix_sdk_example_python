# ConvertToHtmlByPages.py
# Example how to convert PDF to HTML.

# import utils to load required shared libraries
import ctypes
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

htmlParams=PdfHtmlParams()
htmlParams.flags = kHtmlNoExternalCSS | kHtmlNoExternalJS | kHtmlNoExternalIMG| kHtmlNoExternalFONT
#htmlParams.type = kPdfHtmlResponsive
#htmlParams.image_params.format = kImageFormatJpg
#htmlParams.image_params.quality = 80

if not htmlConv.SetParams(htmlParams):
    raise RuntimeError(f'Unable to set HTML conversion parameters: {pdfix.GetError()}')   

docStm = pdfix.CreateFileStream(f"{outputPath}/page_1.html", kPsTruncate)
if not docStm:
    raise RuntimeError(f'Unable to create HTML output file: {pdfix.GetError()}')

# write the head html node with css and javascript
first = bytes("<html>\n<head>\n<title>PDFix sample</title>\n</head>\n<body>\n<script>\n",encoding='ascii')
raw_first = (ctypes.c_ubyte * len(first)).from_buffer_copy(first)
docStm.Write(0, raw_first, len(raw_first))

htmlConv.SaveJavaScript(docStm)

sec = bytes("\n</script>\n<style>\n",encoding='ascii')
raw_sec = (ctypes.c_ubyte * len(sec)).from_buffer_copy(sec)
docStm.Write(docStm.GetSize(), raw_sec, len(raw_sec))

htmlConv.SaveCSS(docStm)

third = bytes("\n</style>\n",encoding='ascii')
raw_third = (ctypes.c_ubyte * len(third)).from_buffer_copy(third)
docStm.Write(docStm.GetSize(), raw_third, len(raw_third))

# save the main document node and one page
for i in range(0, doc.GetNumPages()):
    if  not htmlConv.AddPage(i):
        raise RuntimeError(f'Unable to add HTML page: {pdfix.GetError()}')
    break

# do not save the head node, just document and pages
htmlParams.flags |= kHtmlNoHeadNode;

if not htmlConv.SaveToStream(docStm):
    raise RuntimeError(f'Unable to save HTML document: {pdfix.GetError()}')

# write terminal html
last = bytes("</body>\n</html>",encoding='ascii')
raw_last = (ctypes.c_ubyte * len(last)).from_buffer_copy(last)
docStm.Write(docStm.GetSize(), raw_last, len(raw_last))

docStm.Destroy()

doc.Close()