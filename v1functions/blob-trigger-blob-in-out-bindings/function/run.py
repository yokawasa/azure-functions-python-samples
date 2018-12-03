# -*- coding: utf-8 -*-

"""

Azure Functions Blob Trigger Python Sample
- Simple reading file from Azure Blob Storage and write an output file to Azure Blob Storage

"""

import os

# Read inputfile given from ENV variable named 'inputBlob'
input_file = open(os.environ['inputBlob'], 'r')
clear_text = input_file.read()
input_file.close()

# Encrypt text with ROT13 encryption
encrypted_text= clear_text.decode('rot13')

# Output the modified file to a separate folder in the Storage Blob
output_file = open(os.environ['outputBlob'], 'w')
output_file.write(encrypted_text)
output_file.close()

