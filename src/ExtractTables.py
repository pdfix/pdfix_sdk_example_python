# ExtractTables.py
# Example how to extract tables from PDF.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk import *

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
        output.write("\"")
    else:
        count = element.GetNumChildren()
        if count == 0:
            return
        for i in range(0, count):
            child = element.GetChild(i)
            if child is not None: 
                GetText(child, output)

tableIndex = 1
def SaveTable(element):
    global tableIndex, outputPath
    elem_type = element.GetType()
    if (elem_type == kPdeTable):
        table = PdeTable(element.obj)

        path = outputPath + "/ExtractTables_" + str(tableIndex) + ".csv"
        tableIndex += 1
        output = open(path, "w")
        row_count = table.GetNumRows()
        col_count = table.GetNumCols()

        for row in range(row_count):
            for col in range(col_count):
                cell = table.GetCell(row, col)
                if not cell:
                    continue
                row_span = cell.GetRowSpan()
                col_span = cell.GetColSpan()

                count = cell.GetNumChildren()
                if ((row_span != 0) and (col_span != 0) and (count > 0)):
                    output.write("\"")
                    for i in range(count):
                        child = cell.GetChild(i)
                        if ((child.GetType() == kPdeText) and (child is not None)):
                            GetText(child, output)
                        if (i < count):
                            output.write("")

                output.write(",")

            if (col < col_count):
                output.write("\n")

        if (row < row_count):
            output.write("\"")

        output.close()
        
    else:
        count = element.GetNumChildren()
        if (count == 0):
            return
        for i in range(count):
            child = element.GetChild(i)
            if child:
                SaveTable(child)

for i in range(0, doc.GetNumPages()):
    # acquire page
    page = doc.AcquirePage(i)    
    if page is None:
        raise Exception('Acquire Page fail : ' + pdfix.GetErrorType())
    
    # get the page map of the current page
    pageMap = page.AcquirePageMap()    
    if pageMap is None:
        raise Exception('Acquire PageMap fail: ' + pdfix.GetError())
    if not pageMap.CreateElements():
        raise Exception('Acquire PageMap fail: ' + pdfix.GetError())
    
    # get page container
    container = pageMap.GetElement()
    if container is None:
        raise Exception('Get page element failure : ' + pdfix.GetErrorType())
    
    SaveTable(container)
    page.Release()

print(str(tableIndex - 1) + " tables found")
doc.Close()
