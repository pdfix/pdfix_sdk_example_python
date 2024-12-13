# EditTagProperties.py
# Example how to read and edit tag (PdsStructElement) properties

from Utils import inputPath, outputPath
from pdfixsdk import *
import uuid

pdfix = GetPdfix()

def process_struct_elem(elem: PdsStructElement):
  # read tag properties 
  print(f"{elem.GetType(False)}")        # type [P, L, Table, ...]
  alt = elem.GetAlt()                   # alt text
  id = elem.GetId()                     # id
  for i in range(elem.GetNumPages()):   # multiple pages can appear if tag spans across multiple pages
    page_num = elem.GetPageNumber(i)    # get the page number. can return -1 if tag is invalid
    bbox = elem.GetBBox(page_num)       # get bounding box on a page

  # update tag properties
  elem.SetId(f"{uuid.uuid4()}")   # update id
  if elem.GetType(True) == "P": 
    elem.SetType("H1")              # change type eg P -> H1
  elem.SetAlt(f"This is alt text of the tag with id: {elem.GetId()}")
  elem.SetActualText(f"This is actual text of the tag with id: {elem.GetId()}")

  # process children
  for i in range(elem.GetNumChildren()):
    child_type = elem.GetChildType(i)
    if child_type == kPdsStructChildElement:          # child is struct element (tag)
      obj = elem.GetChildObject(i)
      child_elem = elem.GetStructTree().GetStructElementFromObject(obj)      
      process_struct_elem(child_elem)
      pass  
    elif child_type == kPdsStructChildObject:         # child is OBJR
      pass
    elif child_type == kPdsStructChildPageContent:    # child is MCID or MCR
      pass
    elif child_type == kPdsStructChildStreamContent:  # child is stream object
      pass


doc = pdfix.OpenDoc(inputPath + "/tagged.pdf", "")

struct_tree = doc.GetStructTree()
for i in range(struct_tree.GetNumChildren()):
  obj = struct_tree.GetChildObject(i)
  elem = struct_tree.GetStructElementFromObject(obj)
  process_struct_elem(elem)

doc.Save(outputPath + "/EditTagProperties.pdf", kSaveFull)
