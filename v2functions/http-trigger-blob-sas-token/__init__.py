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
{"token": "sv=2018-03-28&ss=b&srt=o&sp=rl&se=2019-03-29T14%3A02%3A37Z&st=2019-03-29T11%3A57%3A37Z&spr=https&sig=Sh7RAa5MZBk7gfv0haCbEbllFXoiOWJDK9itzPeqURE%3D", "url": "https://azfuncv2linuxstore.blob.core.windows.net/functiontest/sample.jpg?sv=2018-03-28&ss=b&srt=o&sp=rl&se=2019-03-29T14%3A02%3A37Z&st=2019-03-29T11%3A57%3A37Z&spr=https&sig=Sh7RAa5MZBk7gfv0haCbEbllFXoiOWJDK9itzPeqURE%3D" }

"""
import os
import json
import base64
import hmac
import hashlib
import urllib.parse
from datetime import datetime, timedelta

import logging
import azure.functions as func

_ALLOWED_HTTP_METHOD = "POST"
_AZURE_STORAGE_API_VERSION = "2018-03-28"
_AZURE_STORAGE_CONN_STRING_ENV_NAME = "MyStorageConnectionString"
_SAS_TOKEN_DEFAULT_TTL = 1

connString = os.environ[_AZURE_STORAGE_CONN_STRING_ENV_NAME]

def write_http_response(status, body_dict):
    return_dict = {
        "status": status,
        "body": json.dumps(body_dict),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    return json.dumps(return_dict)
    #return func.HttpResponse(
    #        json.dumps(return_dict),
    #        status_code=status
    #    )

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
    hash =hmac.new(
            base64.b64decode(storage_key),
            inputvalue.encode(encoding='utf-8'),
            hashlib.sha256
        ).digest()

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
    sastoken = urllib.parse.urlencode(querystring)

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

def main(req: func.HttpRequest) -> str:
    logging.info('Python HTTP trigger function processed a request.')

    # Get Azure Storage Connection String
    storage_account = None
    storage_key = None

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
        return write_http_response(
            400,
            { 'message': 'Function configuration error: NO Azure Storage connection string found!' }
        )  

    # Check HTTP Mehtod
    if req.method.lower() !=_ALLOWED_HTTP_METHOD.lower():
        return write_http_response(
            405, 
            { 'message': 'Only POST HTTP Method is allowed' }
        )

    permission = None
    container_name = None
    blob_name = None
    try:
        req_body = req.get_json()
    except ValueError:
        # Case: Empty body
        return write_http_response(
            400,
            { 'message': 'Invalid HTTP request body' }
        )
    else:
        # Case: Exception raised in get_json()
        if not 'req_body' in locals():
            return write_http_response(
                400,
                { 'message': 'Invalid HTTP request body' }
            )
        # Case: Invalid parameters
        if not req_body.get('permission') or not req_body.get('container'):
            return write_http_response(
                400,
                { 'message': 'Permission and container parameters must be included in HTTP request body' }
            )

    permission = req_body.get('permission')
    container_name = req_body.get('container')
    blob_name = req_body.get('blobname')
    token_ttl = _SAS_TOKEN_DEFAULT_TTL
    if req_body.get('ttl'):
        token_ttl = int(req_body.get('ttl'))
        if token_ttl < 1:
            return write_http_response(
                400,
                { 'message': 'Token ttl must be digit and more than 0' }
            )

    # Generate SAS Token
    token_dict = generate_sas_token(
                        storage_account,
                        storage_key, 
                        permission, 
                        token_ttl, 
                        container_name, 
                        blob_name 
                    )  
    logging.info("Generated Token token=>{} url=>{}".format(token_dict['token'], token_dict['url']))

    # Write HTTP Response
    return write_http_response(200, token_dict)
