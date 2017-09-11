# -*- coding: utf-8 -*-
#
# install pre-requisite package
# pip install azure-servicebus
#

import json
from azure.servicebus import ServiceBusService

eventhub_namespace="yoichika-eventhub01"
entity="functionshub"
sasKeyName = "rootfunctionshub"
sasKeyValue="XhKPoLKhuhrL8N8KTuhgGNpSGqpUHvQUkA88w3yomt4="

sbs = ServiceBusService(eventhub_namespace, shared_access_key_name=sasKeyName, shared_access_key_value=sasKeyValue)
message = {
    "deviceId": "myDevice001",
    "temperature": "13.5" 
    }
sbs.send_event(entity, json.dumps(message))
