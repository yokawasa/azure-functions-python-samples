# -*- coding: utf-8 -*-

"""

Azure Functions Queue Trigger Python Sample
- Tagging image files stored on Azure Blob Storage by using Cognitive Vision API

"""

import os,sys
import json
from datetime import datetime, timedelta
import httplib, urllib, base64
import base64
import hmac
import hashlib

STORAGE_ACCOUNT_NAME = '<Azure Storage Account Name>'
STORAGE_ACCOUNT_KEY = '<Azure Storage Account Key>'
CONTAINER_NAME = '<Container Name>'
AZURE_STORAGE_VERSION = "2015-12-11"
COGNITIVE_SUBSCRIPTION_KEY = '<Cognitive Services Subscription Key (Vision API) >'

######################### 1: READ QUEUE MESSAGE ###############################
blob_name = open(os.environ['inputMessage']).read()
print "Python script processes blob name: '{0}'".format(blob_name)

######################### 2: GET BLOB SAS URL #################################
st= str(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))
se= str((datetime.utcnow() + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ"))
iv = "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n".format(
        STORAGE_ACCOUNT_NAME,   # 0. account name
        'r',                    # 1. signed permissions
        'b',                    # 2. signed service
        'o',                    # 3. signed resource type
        st,                     # 4. signed start time
        se,                     # 5. signed expire time
        '',                     # 6. signed ip
        'https',                # 7. signed protocol
        AZURE_STORAGE_VERSION)  # 8. signed version

# Create base64 encoded signature
hash =hmac.new(base64.b64decode(STORAGE_ACCOUNT_KEY),iv,hashlib.sha256).digest()
sig = base64.b64encode(hash)
querystring = {
    'sv':AZURE_STORAGE_VERSION,'ss':'b','srt':'o','sp':'r','se':se,'st':st,'spr':'https','sig':sig }
blob_url = "https://{0}.blob.core.windows.net/{1}/{2}?{3}".format(
         STORAGE_ACCOUNT_NAME,
         CONTAINER_NAME,
         blob_name,
         urllib.urlencode(querystring) )
print "Blob SAS URL: " + blob_url

##################### 3: COGNITIVE SERIVICE PROCESSING (GET TAGS) ############
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': COGNITIVE_SUBSCRIPTION_KEY,
}
params = urllib.urlencode({})
body = json.dumps( {"url": blob_url})
r_data = ''
try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/tag?%s" % params, body, headers)
    response = conn.getresponse()
    r_data = response.read()
    print(r_data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

if r_data:
    r_jsonobject=json.loads(r_data)
    tags = []
    for tag_dict in r_jsonobject['tags']:
        tags.append(tag_dict['name'])
    outdoc= {
        "blob_name": blob_name,
        "tags": ','.join(tags)
    }
    print outdoc
