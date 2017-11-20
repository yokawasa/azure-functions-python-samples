# -*- coding: utf-8 -*-

"""

Azure Functions HTTP Trigger Python Sample
- Get RSS feed URL from HTTP Post and add it onto Queue

"""

import os
import json

## Open HTTP Handle + Get Post Data
postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')

## Out Queue Open and Write feedurl + Close
if 'feedurl' not in postreqdata:
    print ("No feedurl included in request body!")
    response.write("NG: No feedurl included in request body!")
else:
    outqueue = open(os.environ['outputQueueItem'], 'w')
    outqueue.write(postreqdata['feedurl'])
    outqueue.close()
    response.write("OK")

## Close HTTP Handle
response.close()
