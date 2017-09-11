# eventhub-trigger-table-out-bindings
Azure Functions EventHub Trigger Python Sample that read message (device info) in EventHub that sent from sender and write an output record to Azure Table Storage using Azure Table bindings

| Trigger | In/Out Bindings |
------------ | ----------- |
| EventHub Trigger | output:Table |


## Pre-requisites

 * **Azure EventHub Account**: You need an EventHub account to which you send an event which which Azure functions triggers the functions.
 * **Azure Storage Account (General Purpose Type)**: You need an Azure Storage account as the function read device info in EventHub which is originally sent from sender and store them into your Table.

## Bindings Configuration

You need to configure 2 kinds of bindings: (1) EventHub Trigger (2) Azure Table output Binding. You can configure them either by directly editing function.json file or via Azure Functions' "Function Apps - Functions - Integrate" UI in Azure Portal

```
{
  "bindings": [
    {
      "type": "eventHubTrigger",
      "name": "myEventHubMessage",
      "path": "<eventhub-entitiy-name>",
      "consumerGroup": "$Default",
      "connection": "<eventhub-namespace>_<SAS-policy-name>_EVENTHUB",
      "cardinality": "one",
      "direction": "in"
    },
    {
      "type": "table",
      "name": "outputTable",
      "tableName": "<table-name>",
      "connection": "<storage-account-name>_STORAGE",
      "direction": "out"
    }
  ],
  "disabled": false
}
```



## Test Command

send-event.py is a test command that allows you to send device info to your Eventhub

```
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
```

