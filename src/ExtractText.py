# ExtractText.py
# Example how to extract text from PDF.

from pdfixsdk import *

from Utils import inputPath, outputPath


def GetText(element, output):
    elemType = element.GetType()
    if kPdeText == elemType:
        textElem = PdeText(element.obj)
        text = textElem.GetText()
        output.write(text)
        output.write("\n")
    else:
        count = element.GetNumChildren()
        if count == 0:
            return
        for i in range(0, count):
            child = element.GetChild(i)
            if child is not None:
                GetText(child, output)


pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(f"{inputPath}/test.pdf", "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# prepare the output file
output = open(f"{outputPath}/ExtractText.txt", "w")

for i in range(0, doc.GetNumPages()):
    # acquire page
    page = doc.AcquirePage(i)
    if page is None:
        raise RuntimeError(f"Unable to acquire page: {pdfix.GetError()}")

    # get the page map of the current page
    pageMap = page.AcquirePageMap()
    if pageMap is None:
        raise RuntimeError(f"Unable to acquire page map: {pdfix.GetError()}")
    if not pageMap.CreateElements():
        raise RuntimeError(f"Unable to acquire page map: {pdfix.GetError()}")

    # get page container
    container = pageMap.GetElement()
    if container is None:
        raise RuntimeError(f"Unable to get page element: {pdfix.GetError()}")
    GetText(container, output)

    pageMap.Release()
    page.Release()

output.close()
doc.Close()
