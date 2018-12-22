import logging
import azure.functions as func
import json

def _rot13(c):
    if 'A' <= c and c <= 'Z':
        return chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
    if 'a' <= c and c <= 'z':
        return chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
    return c

def process_rot13(s):
    g = (_rot13(c) for c in s)
    return ''.join(g)

def main(documents: func.DocumentList, outdoc: func.Out[func.Document]) -> str:
 
    for document in documents:
        logging.info(document.to_json())

        ## Process Something
        clear_text = document["text"]
        encrypted_text= process_rot13(clear_text)        

        ## Create output data
        newdocument = {
            "name": document["name"],
            "text": encrypted_text 
        }
        ## Store output data using Cosmos DB output binding
        outdoc.set(func.Document.from_json(json.dumps(newdocument)))