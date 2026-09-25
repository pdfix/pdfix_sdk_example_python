# EnumerateTags.py
# Example how to enumerate Figure tags using PdfDoc.EnumStructTree.

from pdfixsdk import (
    GetPdfix,
    PdfStructElemEnumProcType,  # This will work in next SDK version
    PdsStructElement,
    kEnumNone,
    kEnumResultContinue,
    kPdsStructChildElement,
)

from Utils import input_path

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path.joinpath("test.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

struct_tree = doc.GetStructTree()
if struct_tree is None:
    raise RuntimeError(f"Unable to get structure tree: {pdfix.GetError()}")

figures: list[PdsStructElement] = []


@PdfStructElemEnumProcType
def enum_figure_tags(_doc_ptr, parent_ptr, index, _client_data):
    parent = PdsStructElement(parent_ptr)
    if parent.GetChildType(index) != kPdsStructChildElement:
        return kEnumResultContinue

    obj = parent.GetChildObject(index)
    elem = struct_tree.GetStructElementFromObject(obj)
    if elem.GetType(False) != "Figure":
        return kEnumResultContinue

    alt = elem.GetAlt()
    print(f"Figure {len(figures) + 1}:")
    for i in range(elem.GetNumPages()):
        page_num = elem.GetPageNumber(i)
        bbox = elem.GetBBox(page_num)
        print(f"  page={page_num}")
        print(
            "  bbox="
            f"({bbox.left:.2f}, {bbox.bottom:.2f}, {bbox.right:.2f}, {bbox.top:.2f})"
        )
    print(f"  alt={alt!r}")
    figures.append(elem)
    return kEnumResultContinue


doc.EnumStructTree(None, kEnumNone, enum_figure_tags, None)

if not figures:
    print("No Figure tags found.")

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
