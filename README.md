# PDFix SDK example for python
For more information please visit [https://pdfix.net](https://pdfix.net).

## Installation
Initialize and activate python virtual environment
```
python3 -m venv env
```

Linux, macOS
```
source env/bin/activate
```
Windows
```
env/Scripts/activate
```

### Installation using requirements
```
pip install -r requirements.txt
```

### Manual installation
```
pip3 install pdfix-sdk
```

## Code Example
```
from pdfixsdk.Pdfix import *

pdfix  = GetPdfix()
doc = pdfix.OpenDoc("test.pdf", "")
print("Number of pages: " + str(doc.GetNumPages()))
doc.close()

```

## Have a question? Need help?
Let us know and we’ll get back to you. Write us to support@pdfix.net or fill the [contact form](https://pdfix.net/support/).
