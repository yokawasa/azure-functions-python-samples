# -*- coding: utf-8 -*-

"""
Azure Functions Queue Trigger
- Get a document ID from Queue as a queue message, select a document object from Cosmos DB by using the document ID, and finally dump the object
"""

import os
import sys
import json

def functions_process(doc):
    print(doc)

def functions_main():
    ## function's starting point
    print ("Starting the operation...")
    cosmosdb_data = open(os.environ['inputDocument']).read()
    docs=json.loads(cosmosdb_data)
    if len(docs) < 1:
        errorlog("No documents obtained via Azure Function Queue & CosmosDB binding")
        sys.exit(0)
    doc = docs[0]
    
    ## process doc
    print ("Processing document")
    functions_process(doc)

    ## Output results if needed
    print ("The end of operation")

functions_main()
