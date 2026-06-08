# TagLink.py
# Example how to create and tag a Link anotation with URI action.

from pdfixsdk import *

from Utils import input_path, output_path

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path.joinpath("test.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

page = doc.AcquirePage(0)
if page is None:
    raise RuntimeError(f"Unable to acquire page: {pdfix.GetError()}")

# define link annotation bounding box
bbox = PdfRect()
bbox.left = 100
bbox.bottom = 400
bbox.right = bbox.left + 100
bbox.top = bbox.bottom + 200

# create Link annotation
annot = page.CreateAnnot(kAnnotLink, bbox)
if annot is None:
    raise RuntimeError(pdfix.GetError())
page.AddAnnot(-1, annot)
link = PdfLinkAnnot(annot.obj)

# set annotation border style (invisible)
annot_dict = annot.GetObject()
border_dict = annot_dict.PutDict("BS")
border_dict.PutName("S", "S")
border_dict.PutName("Type", "Border")
border_dict.PutNumber("W", 0)

# create link action (URI)
action = doc.CreateAction(kActionURI)
if action is None:
    raise RuntimeError(pdfix.GetError())
action_dict = PdsDictionary(action.GetObject().obj)
action_dict.PutString("URI", "www.pdfix.net")
link.SetAction(action)

# create Link tag
struct_tree = doc.GetStructTree()
if struct_tree is None:
    struct_tree = doc.CreateStructTree()

# add Link struct element directly under the Document tag
struct_elem_root = struct_tree.GetStructElementFromObject(struct_tree.GetObject())
if struct_elem_root.GetNumChildren() == 0:
    struct_elem_doc = struct_elem_root.AddNewChild("Document", 0)
else:
    struct_elem_doc_obj = struct_elem_root.GetChildObject(0)
    struct_elem_doc = struct_tree.GetStructElementFromObject(struct_elem_doc_obj)

# create a Link tag
struct_elem_link = struct_elem_doc.AddNewChild("Link", 0)

# Add link annotation OBJR using PdsObject
struct_elem_link_obj = (
    struct_elem_link.GetObject()
)  # access the struct element dictionary
struct_elem_link_obj.Put("Pg", page.GetObject())  # Pg reference
struct_elem_objr = struct_elem_link_obj.PutDict("K")  # Add kid object
struct_elem_objr.Put("Obj", annot_dict)  # Object reference
struct_elem_objr.Put("P", struct_elem_link_obj)  # Parent object reference
struct_elem_objr.PutName("Type", "OBJR")  # Type OBJR

page.Release()

if not doc.Save(output_path.joinpath("TagLink.pdf").as_posix(), kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
