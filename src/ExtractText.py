# ExtractText.py
# Example how to extract text from PDF.

# import initialization to load required shared libraries
from Initialization import inputPath, outputPath
from Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

def GetText (element, output):
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
            
# prepare the output file
output = open(outputPath + "/ExtractText.txt", "w")

for i in range(0, doc.GetNumPages()):
    # acquire page
    page = doc.AcquirePage(i)
    if page is None:
        raise Exception('Acquire Page fail : ' + pdfix.GetError())

    # get the page map of the current page
    pageMap = page.AcquirePageMap(0, None)
    if pageMap is None:
        raise Exception('Acquire PageMap fail : ' + pdfix.GetError())

    # get page container
    container = pageMap.GetElement()
    if container is None:
        raise Exception('Get page element failure : ' + pdfix.GetError())
    GetText(container, output)
 
output.close()    
doc.Close()
