# Utils.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

import platform, sys

# license information
# for evaluation purpose please generate trial license key on this
# website https://pdfix.net/download

def getEmail():
    if len(sys.argv) >= 2:  # if email passed as the first argument
        return sys.argv[1]
    return "yourEmail"

def getLicenseKey():
    if len(sys.argv) >= 3:  # if license key passed as the second argument
        return sys.argv[2]
    return "yourLicenseKey"

# binaries path and name based on platform
pdfix_dll_name = None           # Pdfix module
pdftohtml_dll_name = None       # PdfToHtml module

def getModuleName(module):
    pltfm = platform.system()
    if pltfm == 'Darwin':
        return 'lib' + module + '64.dylib'
    elif pltfm == "Windows":
        return module + '.dll'
    elif pltfm == "Linux":
        return 'lib' + module + '64.so'
