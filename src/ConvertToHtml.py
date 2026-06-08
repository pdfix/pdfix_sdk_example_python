# ConvertToHtml.py
# Example how to convert PDF to HTML.

from pdfixsdk import *

from Utils import input_path, output_path

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path.joinpath("test.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

htmlConv = doc.CreateHtmlConversion()
if htmlConv is None:
    raise RuntimeError(f"Unable to create HTML conversion: {pdfix.GetError()}")

# convert all pages at once
htmlParams = PdfHtmlParams()
htmlParams.flags = kHtmlNoExternalCSS | kHtmlNoExternalJS | kHtmlNoExternalIMG
if not htmlConv.SetParams(htmlParams):
    raise RuntimeError(f"Unable to set HTML conversion parameters: {pdfix.GetError()}")
if not htmlConv.Save(output_path.joinpath("index.html").as_posix()):
    raise RuntimeError(f"Unable to save HTML document: {pdfix.GetError()}")

htmlConv.Destroy()
doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
