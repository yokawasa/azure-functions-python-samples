# -*- coding: utf-8 -*-

"""
An HTTP trigger Azure Function that returns a SAS token for Azure Storage for the specified container and blob name. 
You can also specify access permissions for the container/blob name and optionally its token time-to-live period.
The SAS token expires in an hour by default.

[HTTP Request body format]
HTTP Request body must include the following parameters:
{
    'permission': '<Signed permission for shared access signature (Required)>',
    'container': '<Container name to access (Required)>',
    'blobname': '<Blob object name to access (Optional)>'
    'ttl': '<Token time to live period in hours. 1hour by default (Optional)>'
 }

The following values can be used for permissions: 
    "a" (Add), "r" (Read), "w" (Write), "d" (Delete), "l" (List)
Concatenate multiple permissions, such as "rwa" = Read, Write, Add

Sample Request Body
 {
    'permission': "rl",
    'container': "functions",
    'blobname': "yokawasa.png"
 }

[Response body format]
HTTP response body format is:
{
    'token': '<Shared Access Signature Token string>',
    'url' :  '<SAS resource URI>'
}

Sample Response Body
{'url': 'https://testfunction.blob.core.windows.net/functiontest/yokawasa.png?sig=sXBjML1Fpk9UnTBtajo05ZTFSk0LWFGvARZ6WlVcAog%3D&srt=o&ss=b&spr=https&sp=rl&sv=2016-05-31&se=2017-07-01T00%3A21%3A38Z&st=2017-07-01T23%3A16%3A38Z', 'token': 'sig=sXBjML1Fpk9UnTBtajo05ZTFSk0LWFGvARZ6WlVcAog%3D&srt=o&ss=b&spr=https&sp=rl&sv=2016-05-31&se=2017-07-01T00%3A21%3A38Z&st=2017-07-01T23%3A16%3A38Z'}

"""
import sys
import os
import json
import base64
import hmac
import hashlib
import urllib
from datetime import datetime, timedelta

_ALLOWED_HTTP_METHOD = "POST"
_AZURE_STORAGE_API_VERSION = "2016-05-31"
_AZURE_STORAGE_CONN_STRING_ENV_NAME = "AZUREWEBJOBSSTORAGE"
_AZURE_FUNCTION_HTTP_INPUT_ENV_NAME = "req"
_AZURE_FUNCTION_HTTP_OUTPUT_ENV_NAME = "res"
_SAS_TOKEN_DEFAULT_TTL = 1

def write_http_response(status, body_dict):
    return_dict = {
        "status": status,
        "body": json.dumps(body_dict),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    output = open(os.environ[_AZURE_FUNCTION_HTTP_OUTPUT_ENV_NAME], 'w')
    output.write(json.dumps(return_dict))

def generate_sas_token (storage_account, storage_key, permission, token_ttl, container_name, blob_name = None ):
    sp = permission
    # Set start time to five minutes ago to avoid clock skew.
    st= str((datetime.utcnow() - timedelta(minutes=5) ).strftime("%Y-%m-%dT%H:%M:%SZ"))
    se= str((datetime.utcnow() + timedelta(hours=token_ttl)).strftime("%Y-%m-%dT%H:%M:%SZ"))
    srt = 'o' if blob_name else 'co'

    # Construct input value
    inputvalue = "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n".format(
        storage_account,  # 0. account name
        sp,                   # 1. signed permission (sp)
        'b',                  # 2. signed service (ss)
        srt,                  # 3. signed resource type (srt)
        st,                   # 4. signed start time (st)
        se,                   # 5. signed expire time (se)
        '',                   # 6. signed ip
        'https',              # 7. signed protocol
        _AZURE_STORAGE_API_VERSION)  # 8. signed version

    # Create base64 encoded signature
    hash =hmac.new(base64.b64decode(storage_key),inputvalue,hashlib.sha256).digest()
    sig = base64.b64encode(hash)

    querystring = {
        'sv':  _AZURE_STORAGE_API_VERSION,
        'ss':  'b',
        'srt': srt,
        'sp': sp,
        'se': se,
        'st': st,
        'spr': 'https',
        'sig': sig,
    }
    sastoken = urllib.urlencode(querystring)

    sas_url = None
    if blob_name:
        sas_url = "https://{0}.blob.core.windows.net/{1}/{2}?{3}".format(
            storage_account,
            container_name,
            blob_name,
            sastoken)
    else:
        sas_url = "https://{0}.blob.core.windows.net/{1}?{2}".format(
            storage_account,
            container_name,
            sastoken)

    return {
            'token': sastoken,
            'url' : sas_url
           }

# Get HTTP Method
env = os.environ
DEFAULT_METHOD = "GET"
http_method = env['REQ_METHOD'] if env.has_key('REQ_METHOD') else DEFAULT_METHOD
print("http_method={}".format(http_method))

# Get Azure Storage Connection String
storage_account = None
storage_key = None
connString = env[_AZURE_STORAGE_CONN_STRING_ENV_NAME]
print("connString={}".format(connString))
ll = connString.split(';')
for l in ll:
    ss = l.split('=',1)
    if len(ss) != 2:
        continue
    if ss[0] == 'AccountName':
       storage_account = ss[1] 
    if ss[0] == 'AccountKey':
       storage_key = ss[1] 
if not storage_account or not storage_key:
    write_http_response(400, 
        { 'message': 'Function configuration error: NO Azure Storage connection string found!' }
    )  
    sys.exit(0)

# Check HTTP Mehtod
if http_method.lower() !=_ALLOWED_HTTP_METHOD.lower():
    write_http_response(405, 
        { 'message': 'Only POST HTTP Method is allowed' }
    )  
    sys.exit(0)

# Get Request Parameters: permission, container, blobname (optional)
req_body_s = open(env[_AZURE_FUNCTION_HTTP_INPUT_ENV_NAME], "r").read()
print("REQUEST BODY => {}".format(req_body_s))
req_body_dict = json.loads(req_body_s)
if "permission" not in req_body_s or "container" not in req_body_s:
    write_http_response(400, 
        { 'message': 'Permission and container parameters must be included in HTTP request body' }
    )  
    sys.exit(0)

permission = req_body_dict['permission']
container_name = req_body_dict['container']
blob_name = None
if "blobname" in req_body_dict:
    blob_name = req_body_dict['blobname']
token_ttl = _SAS_TOKEN_DEFAULT_TTL
if "ttl" in req_body_dict:
    token_ttl = int(req_body_dict['ttl'])
    if token_ttl < 1:
        write_http_response(400, 
            { 'message': 'Token ttl must be digit and more than 0' }
        )  
        sys.exit(0)

# Generate SAS Token
token_dict = generate_sas_token(storage_account, storage_key, permission, token_ttl, container_name, blob_name )  
print("Generated Token token={} url={}".format(token_dict['token'], token_dict['url']))

# Write HTTP Response
write_http_response(200, token_dict)

sys.exit(0)
