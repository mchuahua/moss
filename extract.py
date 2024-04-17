# Usage:
#  - Replace rootPath with folder containing zip files
#  - Assumes all zip files are valid to be extracted (ie. no corrupt zip files)
#  - `py extract.py`

import zipfile,fnmatch,os, re

rootPath = r"/Users/martin/Downloads/submissions/students"
pattern = '*.zip'

for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
        zipfile.ZipFile(os.path.join(root,     filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))

