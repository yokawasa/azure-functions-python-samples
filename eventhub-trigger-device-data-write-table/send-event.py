# -*- coding: utf-8 -*-
#
# install pre-requisite package
# pip install azure-servicebus
#

import json
from azure.servicebus import ServiceBusService

eventhub_namespace="<Eventhub Top Level Namespace>"
entity= "<Eventhub Entity Name>"
sasKeyName = "<SAS Policy Name>"
sasKeyValue= "<SAS Key Value>"

sbs = ServiceBusService(eventhub_namespace, shared_access_key_name=sasKeyName, shared_access_key_value=sasKeyValue)
message = {
    "deviceId": "myDevice001",
    "temperature": "13.5" 
    }
sbs.send_event(entity, json.dumps(message))
