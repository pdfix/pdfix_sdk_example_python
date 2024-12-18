# TagLink.py
# Example how to create and tag a Link anotation with URI action.

from pdfixsdk import *
# import utils to load required shared libraries
from Utils import inputPath, outputPath

pdfix = GetPdfix()

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
page = doc.AcquirePage(0)

# define link annotation bounding box
bbox = PdfRect()
bbox.left = 100
bbox.bottom = 400
bbox.right = bbox.left + 100
bbox.top = bbox.bottom + 200

# create Link annotation
annot = page.CreateAnnot(kAnnotLink, bbox)
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
action_dict = PdsDictionary(action.GetObject().obj)
action_dict.PutString("URI", "www.pdfix.net")
link.SetAction(action)

# create Link tag
struct_tree = doc.GetStructTree()
if not struct_tree:
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
struct_elem_link_obj = struct_elem_link.GetObject()     # access the struct element dictionary 
struct_elem_link_obj.Put("Pg", page.GetObject())        # Pg reference
struct_elem_objr = struct_elem_link_obj.PutDict("K")    # Add kid object
struct_elem_objr.Put("Obj", annot_dict)                 # Object reference
struct_elem_objr.Put("P", struct_elem_link_obj)         # Parent object reference
struct_elem_objr.PutName("Type", "OBJR")                # Type OBJR


doc.Save(outputPath + "/TagLink.pdf", kSaveFull)