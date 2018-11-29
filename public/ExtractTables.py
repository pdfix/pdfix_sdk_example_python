# ExtractTables.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

## 
# \page Python_Samples Python Samples
# -\subpage ExtractTables_py 
# \page ExtractTables_py Extract Tables Sample
# Example how to extract tables from PDF.
# \snippet /ExtractTables.py ExtractTables_py

##
# \cond INTERNAL
# ![ExtractTables_py]
import os
import Utils
from Pdfix import *

table_index = 1

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

def SaveTable(element, save_path):
    global table_index
    elem_type = element.GetType()
    if (elem_type == kPdeTable):
        table = PdeTable(element.obj)

        path = save_path + "/ExtractTables_" + str(table_index) + ".csv"
        table_index += 1
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
                SaveTable(child, save_path)

def ExtractTables( email, key,
                open_path,                  # source of PDF document
                save_path,                  # directory where to extract tables
                config_path):               # configuration file (optional)
    
    print("ExtractTables")

    pdfix  = GetPdfix()
    
    if pdfix is None:
        raise Exception('Pdfix Initialization fail')
    
    # authorization
    if not pdfix.Authorize(email, key):
        raise Exception('Authorization fail : ' + pdfix.GetError())
    
    doc = pdfix.OpenDoc(open_path, "")
    if doc is None:
        raise Exception('Unable to open doc : ' + str(pdfix.GetError()))

    numPages = doc.GetNumPages()
    
    for i in range(0, numPages):
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
        
        SaveTable(container, save_path)

        doc.ReleasePage(page)

    
    print(str(table_index - 1) + " tables found")
    doc.Close()
    pdfix.Destroy()
    

try:
    # pdfix initialization
    email = Utils.getEmail()                # email address
    licenseKey = Utils.getLicenseKey()      # license key
    cwd = os.getcwd() + "/"                 # current working directory
    os.makedirs(cwd + 'output')

    # pdfix initialization
    Pdfix_init(cwd + Utils.getModuleName('pdfix'))

    ExtractTables(email, licenseKey, 
        cwd + 'resources/test.pdf', 
        cwd + 'output/',
        cwd + 'resources/config.json')
    
    Pdfix_destroy()
except Exception as e:
    print('Oops! ' + str(e))

##
# ![ExtractTables_py]
# \endcond
