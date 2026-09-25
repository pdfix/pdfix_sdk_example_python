# PDFix SDK example for Python

For more information please visit [https://pdfix.net](https://pdfix.net).

## Installation

Initialize and activate a Python virtual environment:

```bash
python3 -m venv env
```

Linux, macOS:

```bash
source env/bin/activate
```

Windows (PowerShell):

```powershell
.\env\Scripts\Activate.ps1
```

Windows (Command Prompt):

```cmd
env\Scripts\activate.bat
```

### Installation using requirements

```bash
pip install -r requirements.txt
```

### Manual installation

```bash
pip3 install pdfix-sdk
```

## Code example

```python
from pdfixsdk import *

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc("test.pdf", "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

print(f"Number of pages: {doc.GetNumPages()}")
doc.Close()
```

## Other Python projects with PDFix SDK

https://github.com/topics/pdfix-actions

## Have a question? Need help?

Let us know and we’ll get back to you. Write to support@pdfix.net or use the [contact form](https://pdfix.net/support/).
