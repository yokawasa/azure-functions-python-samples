import os

######################### 1: READ QUEUE MESSAGE #############################
blob_name = open(os.environ['inputMessage']).read()
print("Blob file name: '{0}'".format(blob_name))

######################### 2: READ BLOB FILE ##################################
input_file = open(os.environ['inputBlob'], 'r')
clear_text = input_file.read()
input_file.close()
print("Content in the blob file: '{0}'".format(clear_text))

######################### 3: PROCESS THE CONTENT #############################
# Encrypt text with ROT13 encryption
encrypted_text= clear_text.decode('rot13')
print("Encrypted Content: '{0}'".format(encrypted_text))

