# ExtractTables.py
# Example how to extract tables from PDF.

from pdfixsdk import *

from Utils import input_path, output_path


def GetText(element, output):
    elemType = element.GetType()
    if kPdeText == elemType:
        textElem = PdeText(element.obj)
        text = textElem.GetText()
        output.write(text)
        output.write('"')
    else:
        count = element.GetNumChildren()
        if count == 0:
            return
        for i in range(count):
            child = element.GetChild(i)
            if child is not None:
                GetText(child, output)


tableIndex = 1


def SaveTable(element):
    global tableIndex, output_path
    elem_type = element.GetType()
    if elem_type == kPdeTable:
        table = PdeTable(element.obj)

        path = output_path.joinpath(f"ExtractTables_{tableIndex}.csv")
        tableIndex += 1
        row_count = table.GetNumRows()
        col_count = table.GetNumCols()

        with open(path, "w", encoding="utf-8") as output:
            for row in range(row_count):
                for col in range(col_count):
                    cell = table.GetCell(row, col)
                    if not cell:
                        continue
                    row_span = cell.GetRowSpan()
                    col_span = cell.GetColSpan()

                    count = cell.GetNumChildren()
                    if (row_span != 0) and (col_span != 0) and (count > 0):
                        output.write('"')
                        for i in range(count):
                            child = cell.GetChild(i)
                            if (child.GetType() == kPdeText) and (child is not None):
                                GetText(child, output)
                            if i < count:
                                output.write("")

                    output.write(",")

                if col < col_count:
                    output.write("\n")

            if row < row_count:
                output.write('"')

    else:
        count = element.GetNumChildren()
        if count == 0:
            return
        for i in range(count):
            child = element.GetChild(i)
            if child:
                SaveTable(child)


pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path.joinpath("test.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

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

    SaveTable(container)
    pageMap.Release()
    page.Release()

print(f"{tableIndex - 1} tables found")
doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
