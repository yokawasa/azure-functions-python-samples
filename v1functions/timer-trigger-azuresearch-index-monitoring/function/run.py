# -*- coding: utf-8 -*-
"""

Azure Functions Timer Trigger Python Sample 
- Get Azure Search Index Statistics and store them into DocumentDB

DocumentDB binding reference:
https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-documentdb

"""

import sys, os, datetime, json
import httplib, urllib

AZURE_SEARCH_SERVICE_NAME='<azure search service name>'
AZURE_SEARCH_API_VER='<azure search api version: ex. 2015-02-28-Preview>'
AZURE_SEARCH_ADMIN_KEY='<azure search API admin key>'
AZURE_SEARCH_INDEX_NAME='<azure search index name>'
CONTENT_TYPE='application/json'

headers = {
 'api-key': AZURE_SEARCH_ADMIN_KEY,
 'content-type': "application/json"
}

r_data = ''
try:
    conn = httplib.HTTPSConnection('{}.search.windows.net'.format(AZURE_SEARCH_SERVICE_NAME))
    conn.request("GET",
        "/indexes/{0}/stats?api-version={1}".format(AZURE_SEARCH_INDEX_NAME, AZURE_SEARCH_API_VER),
        '', headers)
    response = conn.getresponse()
    r_data = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

if r_data:
    r_jsonobject=json.loads(r_data)
    outdoc= {
        "doccount": r_jsonobject['documentCount'],
        "storagesize": r_jsonobject['storageSize'],
        "timestamp": str(datetime.datetime.utcnow())
    }
    print outdoc
    # Writing to DocumentDB (Document parameter name: outputDocument)
    with open(os.environ['outputDocument'], 'wb') as f:
        json.dump(outdoc,f)
