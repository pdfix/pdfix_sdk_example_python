# ExtractText.py
# Example how to extract text from PDF.

from pdfixsdk import *

from Utils import input_path, output_path


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
        for i in range(count):
            child = element.GetChild(i)
            if child is not None:
                GetText(child, output)


pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path / "test.pdf", "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

with open(output_path / "ExtractText.txt", "w", encoding="utf-8") as output:
    for i in range(doc.GetNumPages()):
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

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
