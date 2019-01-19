# queue-trigger-blob-in-out-binding (Python)

| Sample | Description | Trigger | In Bindings | Out Bindings
| ------------- | ------------- | ------------- | ----------- | ----------- |
| `queue-trigger-blob-in-out-binding` | Azure Functions Queue Trigger Python Sample. The function gets a file name from queue message, reads a blob file named the file name using Blob Input Binding, then ROT13 encodes the obtained clear text, and finally stores it into Azure Blob Storage using Blob Output Binding  | Queue Storage | Blob Storage | Blob Storage |

## Configurations
As specified in `functions.json`, you need Azure Storage account for triggering functions, input & output binding.

```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "name": "myitem",
      "type": "queueTrigger",
      "direction": "in",
      "queueName": "itemsqueue",
      "connection": "MyStorageConnectionString"
    },
    {
      "name": "inputblob",
      "type": "blob",
      "path": "inputitems/{queueTrigger}",
      "connection": "MyStorageConnectionString",
      "direction": "in"
    },
    {
      "name": "outputblob",
      "type": "blob",
      "direction": "out",
      "connection": "MyStorageConnectionString",
      "path": "outputitems/{queueTrigger}"
    }
  ]
}
```

### Create Azure Storage Account

Create an Azure Storage Account
```sh
RESOURCE_GROUP="rg-testfunctions"
REGION="japaneast"
STORAGE_ACCOUNT="teststore"
az storage account create --name $STORAGE_ACCOUNT \
    --location $REGION \
    --resource-group $RESOURCE_GROUP \
    --sku Standard_LRS
```

### Create Blob Storage Containers

Create 2 blob containers in the storage you've created: `inputitems` and `outputitems`
```sh
# Get Storage Key
ACCESS_KEY=$(az storage account keys list --account-name $STORAGE_ACCOUNT --resource-group $RESOURCE_GROUP --output tsv |head -1 | awk '{print $3}')

az storage container create  \
    --name "inputitems" \
    --account-name $STORAGE_ACCOUNT \
    --account-key $ACCESS_KEY

az storage container create  \
    --name "outputitems" \
    --account-name $STORAGE_ACCOUNT \
    --account-key $ACCESS_KEY
```

### Create Queue in Queue Storage

Create a queue in the storage you've created: `itemsqueue`

```sh
# Get Storage Key
ACCESS_KEY=$(az storage account keys list --account-name $STORAGE_ACCOUNT --resource-group $RESOURCE_GROUP --output tsv |head -1 | awk '{print $3}')

az storage queue create \
    --name "itemsqueue" \
    --account-name $STORAGE_ACCOUNT \
    --account-key $ACCESS_KEY
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