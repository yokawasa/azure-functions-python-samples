# -*- coding: utf-8 -*-

"""

Azure Functions HTTP Trigger Python Sample
- Get and dump HTTPS request info that the trigger receives

Special Thanks to anthonyeden for great Python HTTP example:
https://github.com/anthonyeden/Azure-Functions-Python-HTTP-Example

"""

import sys
import os

DEFAULT_METHOD = "GET"

env = os.environ

# Get HTTP METHOD
http_method = env['REQ_METHOD'] if env.has_key('REQ_METHOD') else DEFAULT_METHOD
print "HTTP METHOD => {}".format(http_method)

# Get QUERY STRING
req_url = env['REQ_HEADERS_X-ORIGINAL-URL'] if env.has_key('REQ_HEADERS_X-ORIGINAL-URL') else ''
urlparts =req_url.split('?') 
query_string = urlparts[1] if len(urlparts) == 2 else ''
print "QUERY STRING => {}".format(query_string)

if http_method.lower() == 'post':
    request_body = open(env['req'], "r").read()
    print "REQUEST BODY => {}".format(request_body)

print "Dump ENVIRONMENT VARIABLES:"
for k in env:
    print "ENV: {0} => {1}".format(k, env[k])
