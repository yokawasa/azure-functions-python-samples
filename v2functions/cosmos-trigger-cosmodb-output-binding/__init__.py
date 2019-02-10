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

def main(docs: func.DocumentList, outdoc: func.Out[func.Document]) -> str:

    newdocs = func.DocumentList() 
    for doc in docs:
        logging.info(doc.to_json())

        ## Process Something
        clear_text = doc["text"]
        encrypted_text= process_rot13(clear_text)        

        ## Create a new doc (type:Dict)
        newdoc_dict = {
            "name": doc["name"],
            "text": encrypted_text 
        }

        ## Append the new doc to DocumentList for output
        newdocs.append(func.Document.from_dict(newdoc_dict))
 
    ## Set the DocumentList to outdoc to store into CosmosDB using CosmosDB output binding
    outdoc.set(newdocs)