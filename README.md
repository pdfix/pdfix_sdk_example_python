# PDFix SDK example for python
PDFix SDK code examples 

For more information please visit [https://pdfix.net](https://pdfix.net).

## Installation
```
python3 -m venv env
source env/bin/activate
pip install -i https://test.pypi.org/simple/ pdfix-sdk-pdfix-support
```

## Code 
```
from pdfixsdk.Pdfix import *

pdfix  = GetPdfix()
doc = pdfix.OpenDoc("test.pdf", "")
print("Number of pages: " + str(doc.GetNumPages()))
doc.close()

```
## Have a question? Need help?
Let us know and we’ll get back to you. Write us to support@pdfix.net or fill the [contact form](https://pdfix.net/support/).