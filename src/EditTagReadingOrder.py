# EditTagReadingOrder.py
# Example how to edit the reading order of tags

from Utils import inputPath, outputPath
from pdfixsdk import *

pdfix = GetPdfix()

# process structure elements recursively 
# function returns parent of the found tag and its index within the parent
# or the tag itself
def process_struct_elem(elem: PdsStructElement, tag_type: str, return_parent: bool):

  # process children
  for i in range(elem.GetNumChildren()):
    child_type = elem.GetChildType(i)
    if child_type == kPdsStructChildElement:          # child is struct element (tag)
      obj = elem.GetChildObject(i)
      child_elem = elem.GetStructTree().GetStructElementFromObject(obj)   
      print(f"{child_elem.GetType(True)}")   
      if (child_elem.GetType(True) == tag_type):
        return [elem, i] if return_parent else child_elem     # return [parent_tag, index] or tag
      
    ret = process_struct_elem(child_elem, tag_type, return_parent)
    if ret:
      return ret
  return None

# find tag by type 
# if return_parent is True, return parent tag and chind index of found tag
# if return_parent is False, return only the found tag
def find_tag(struct_tree, tag_type, return_parent):
  root_elem = struct_tree.GetStructElementFromObject(struct_tree.GetObject())
  return process_struct_elem(root_elem, tag_type, return_parent)

doc = pdfix.OpenDoc(inputPath + "/tagged.pdf", "")

struct_tree = doc.GetStructTree()
document_tag = find_tag(struct_tree, "Document", False)         # find Document tag
p_tag_parent, p_tag_index = find_tag(struct_tree, "P", True)    # find parent of first P tag and index within parent


# move found P tag as the first element under Document tag
p_tag_parent.MoveChild(p_tag_index, document_tag, 0)

doc.Save(outputPath + "/EditTagReadingOrder.pdf", kSaveFull)
