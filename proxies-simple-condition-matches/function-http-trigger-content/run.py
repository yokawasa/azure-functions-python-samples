# -*- coding: utf-8 -*-

import sys
import os
import json

_AZURE_FUNCTION_DEFAULT_METHOD = "GET"
_AZURE_FUNCTION_HTTP_INPUT_ENV_NAME = "req"
_AZURE_FUNCTION_HTTP_OUTPUT_ENV_NAME = "res"

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

def get_qs_value(keyname, querystring):
    v = None
    kvsets = querystring.split('&')
    for kvset in kvsets:
        items = kvset.split('=')
        if len(items) == 2 and items[0].lower() == keyname:
            v = items[1]
    return v

env = os.environ

# Get HTTP METHOD
http_method = env['REQ_METHOD'] if env.has_key('REQ_METHOD') else _AZURE_FUNCTION_DEFAULT_METHOD
print "HTTP METHOD => {}".format(http_method)

# Get QUERY STRING
req_url = env['REQ_HEADERS_X-ORIGINAL-URL'] if env.has_key('REQ_HEADERS_X-ORIGINAL-URL') else ''
urlparts =req_url.split('?')
query_string = urlparts[1] if len(urlparts) == 2 else ''
print "QUERY STRING => {}".format(query_string)
content_id = get_qs_value('contentid', query_string)
print "CONTENT ID => {}".format(content_id)

res_body = {}
res_body['contentid'] = content_id

write_http_response(200, res_body)
