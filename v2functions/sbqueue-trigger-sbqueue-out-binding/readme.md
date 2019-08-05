# sbqueue-trigger-sbqueue-out-binding (Python)

| Sample | Description | Trigger | In Bindings | Out Bindings
| ------------- | ------------- | ------------- | ----------- | ----------- |
| `sbqueue-trigger-sbqueue-out-binding` | Azure Functions Service Bus Queue Trigger Python Sample. The function demonstrates reading from a Service Bus queue and placing a new message into a Service Bus queue. | Service Bus Queue | None | Service Bus Queue |

## Configurations

`function.json`:

```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "name": "msgIn",
      "type": "serviceBusTrigger",
      "direction": "in",
      "queueName": "inqueue",
      "connection": "ServiceBusNamespaceConnectionString"
    },
    {
      "name": "msgOut",
      "type": "serviceBus",
      "direction": "out",
      "connection": "ServiceBusNamespaceConnectionString",
      "queueName": "outqueue"
    }
  ]
}
```

### Create the Service Bus Queues

Create two Service Bus Queues in the namespace used in `ServiceBusNamespaceConnectionString`, `inqueue` and `outqueue`:

```sh
az servicebus queue create --name inqueue \
    --resource-group $RESOURCE_GROUP \
    --namespace-name $SERVICEBUS_NAMESPACE

az servicebus queue create --name outqueue \
    --resource-group $RESOURCE_GROUP \
    --namespace-name $SERVICEBUS_NAMESPACE
```

## How to develop and publish the functions

### Local development

```sh
func host start
```

### Publish the function to the cloud

Publish the function to the cloud
```sh
FUNCTION_APP_NAME="MyFunctionApp"
func azure functionapp publish $FUNCTION_APP_NAME --build-native-deps --no-bundler
```

Add Functions App Settings
```sh
FUNCTION_STORAGE_CONNECTION="*************"
az webapp config appsettings set \
  -n $FUNCTION_APP_NAME \
  -g $RESOURCE_GROUP \
  --settings \
    MyStorageConnectionString=$FUNCTION_STORAGE_CONNECTION
```