# -*- coding: utf-8 -*-

"""
Azure Functions Blob Trigger Python Sample
- Reading Zip archived files from Azure Blob Storage
"""

import os
import zipfile

# Read Input Zip file given from ENV variable named 'inputBlob'
zippath=os.environ['inputBlob']
print("Zip File Path: {}".format(zipfilepath))

# Read text files in the given zip file assuming that the files are clear text
with zipfile.ZipFile(zippath) as z:
    for filename in z.namelist():
        print("filename:{} in zipfile:{}".format(filename, zippath))
        if not os.path.isdir(filename):
            # Reading the file in Zipfile
            with z.open(filename) as f:
                for line in f:
                    print(line)
