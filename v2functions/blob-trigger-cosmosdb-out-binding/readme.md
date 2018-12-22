# blob-trigger-cosmosdb-out-binding (Python)

| Sample | Description | Trigger | In Bindings | Out Bindings
| ------------- | ------------- | ------------- | ----------- | ----------- |
| `cosmosdb-trigger-cosmosdb-in-binding` | Azure Functions Blob Storage Trigger Python Sample. The function gets image data from Azure Blob Trigger, gets tags for the image with [Computer Vision API](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) ([Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/)), and store the tags into Azure Cosmos DB by leveraging CosmosDB output binding | Blob Storage | NONE | CosmosDB |

## Configurations
As specified in `functions.json`, you need Azure Storage account for triggering functions and Cosmos DB Account to store data using Cosmos DB output binding

```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "name": "myblob",
      "type": "blobTrigger",
      "direction": "in",
      "path": "upload-images/{name}",
      "connection": "AzureWebJobsStorage"
    },
    {
      "direction": "out",
      "type": "cosmosDB",
      "name": "doc",
      "databaseName": "testdb",
      "collectionName": "testcol01",
      "leaseCollectionName": "leases",
      "createLeaseCollectionIfNotExists": true,
      "connectionStringSetting": "AzureWebJobsCosmosDBConnectionString",
      "createIfNotExists": true
    }
  ]
}

```
### Create Blob Storage account & Container

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

Create a container in the storage you've created
```sh
# Get Storage Key
ACCESS_KEY=$(az storage account keys list --account-name $STORAGE_ACCOUNT --resource-group $RESOURCE_GROUP --output tsv |head -1 | awk '{print $3}')

az storage container create  \
    --name "upload-images" \
    --account-name $STORAGE_ACCOUNT \
    --account-key $ACCESS_KEY
```

### Create Cosmos DB Account and DB & Collection

Create a Cosmos DB Account
```sh
COSMOSDB_ACCOUNT_NAME="azfuncv2db"
RESOURCE_GROUP="RG-azfuncv2"
az cosmosdb create \
    --name $COSMOSDB_ACCOUNT_NAME \
    --kind GlobalDocumentDB \
    --resource-group $RESOURCE_GROUP
```

Create Database and Collection in the Cosmos DB that you've created

```sh
# Get Key
COSMOSDB_KEY=$(az cosmosdb list-keys --name $COSMOSDB_ACCOUNT_NAME --resource-group $RESOURCE_GROUP --output tsv |awk '{print $1}')

# Create Database
DATABASE_NAME="testdb"
az cosmosdb database create \
    --name $COSMOSDB_ACCOUNT_NAME \
    --db-name $DATABASE_NAME \
    --key $COSMOSDB_KEY \
    --resource-group $RESOURCE_GROUP

# Create a container with a partition key and provision 400 RU/s throughput.
COLLECTION_NAME="testcol01"
az cosmosdb collection create \
    --resource-group $RESOURCE_GROUP \
    --collection-name $COLLECTION_NAME \
    --name $COSMOSDB_ACCOUNT_NAME \
    --db-name $DATABASE_NAME \
    --partition-key-path /name \
    --throughput 400

# Create a container for leaves
# 'leaves' need to be a single collection partition
# Please see also: https://github.com/Azure/azure-functions-core-tools/issues/930
LEASES_COLLECTION_NAME="leases"
az cosmosdb collection create \
    --resource-group $RESOURCE_GROUP \
    --collection-name $LEASES_COLLECTION_NAME \
    --name $COSMOSDB_ACCOUNT_NAME \
    --db-name $DATABASE_NAME \
    --throughput 400
```

## How to develop and publish the function
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
COSMOS_DB_CONNECTION="***************"
az webapp config appsettings set \
  -n $FUNCTION_APP_NAME \
  -g $RESOURCE_GROUP \
  --settings \
    AzureWebJobsStorage=$FUNCTION_STORAGE_CONNECTION \
    AzureWebJobsCosmosDBConnectionString=$COSMOS_DB_CONNECTION
```
