# -*- coding: utf-8 -*-

import os
import sys
import json
import uuid

"""
Expected Receiving Body Message:
{
    "deviceId": "myDevice0001",
    "temperature": "10.1"
}
[note]
Use "deviceId" as PartitionKey for Azure table to write

Expected Function's Trigger Configuration:
 - 'trigger': AzureEventHub
 - 'Event hub cardinality': 'One'

Expected Function's Output Configuration:
 - 'output': Azure Table Storage
 - 'Table parameter name: 'outputTable

"""

# Read the EventHub Message 
receivedBody = json.loads(open(os.environ['myEventHubMessage']).read())
print('Received body:', receivedBody)
# -> ('received object:', {u'deviceId': u'myDevice0001', u'temperature': u'10.1'})
if not 'deviceId' in receivedBody or not 'temperature' in receivedBody:
    print("Skip: invalid eventHub body!")
    sys.exit(0)

## Device ID
recordId = str(uuid.uuid4())

outdoc= {
    "PartitionKey": receivedBody['deviceId'], 
    "RowKey": recordId,
    "temperature": receivedBody['temperature']
}
# Writing to Azure Table Storage (Table parameter name: outputTable)
print('Writing data to Azure Table:', outdoc)
with open(os.environ['outputTable'], 'w') as f:
    json.dump(outdoc,f)
