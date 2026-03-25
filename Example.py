import os
import sys
import traceback
import importlib

# add src to path
sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

modules = [
    "AddComment",
    "AddTags",
    "AddTagAsArtifact",
    "AddWatermark",
    "ConvertToHtml",
    "ConvertToHtmlByPages",
    "DocumentMetadata",
    "EditContent",
    "EditPageObjectMCID",
    "EditTagProperties",
    "EditTagReadingOrder",
    "ExtractImages",
    "ExtractTables",
    "ExtractText",
    "MakeAccessible",
    "OpenDocFromStream",
    "RenderPage",
    "PdfToJson",
    "SetFormFieldValue",
    "TagLink",
    "ReplaceFont",
]

failed = []

for module_name in modules:
    print(f"\n=== Running: {module_name} ===")
    try:
        importlib.import_module(module_name)
        print(f"OK: {module_name}")
    except Exception as e:
        print(f"FAILED: {module_name}")
        print(f"Error: {e}")
        traceback.print_exc()
        failed.append(module_name)

print("\n=========================")
if failed:
    print("FAILED MODULES:")
    for m in failed:
        print(f" - {m}")
    sys.exit(1)
else:
    print("ALL MODULES PASSED")