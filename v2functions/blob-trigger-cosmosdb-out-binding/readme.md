# blob-trigger-cosmosdb-out-binding (Python)

| Sample | Description | Trigger | In Bindings | Out Bindings
| ------------- | ------------- | ------------- | ----------- | ----------- |
| `cosmosdb-trigger-cosmosdb-in-binding` | Azure Functions Blob Storage Trigger Python Sample. The function gets image data from Azure Blob Trigger, gets tags for the image with [Computer Vision API](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) ([Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/)), and store the tags into Azure Cosmos DB by leveraging CosmosDB output binding | Blob Storage | NONE | CosmosDB |

<!-- TOC -->
- [blob-trigger-cosmosdb-out-binding (Python)](#blob-trigger-cosmosdb-out-binding-python)
  - [Configurations](#configurations)
    - [Create Computer Vision resource](#create-computer-vision-resource)
    - [Create Blob Storage account & Container](#create-blob-storage-account--container)
    - [Create Cosmos DB Account and DB & Collection](#create-cosmos-db-account-and-db--collection)
  - [How to develop and publish the function](#how-to-develop-and-publish-the-function)
    - [Local development](#local-development)
    - [Publish the function to the cloud](#publish-the-function-to-the-cloud)
  - [Test Request](#test-request)
    - [HTTP Request body format](#http-request-body-format)
  - [Response body format](#response-body-format)

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
      "connection": "MyStorageConnectionString"
    },
    {
      "direction": "out",
      "type": "cosmosDB",
      "name": "doc",
      "databaseName": "testdb",
      "collectionName": "testcol01",
      "leaseCollectionName": "leases",
      "createLeaseCollectionIfNotExists": true,
      "connectionStringSetting": "MyCosmosDBConnectionString",
      "createIfNotExists": true
    }
  ]
}
```

### Create Computer Vision resource

First, create a Computer Vision resource

```bash
COGNITIVE_RESOURCE_GROUP="rg_cognitive_test"
REGION="eastasia"
COGNITIVE_ACCOUNT_NAME="mycompvision001"

echo "Create Resource Group: $COGNITIVE_RESOURCE_GROUP"
az group create --name $COGNITIVE_RESOURCE_GROUP --location $REGION

echo "Create Cognitive Resource for Computer Vision: $COGNITIVE_ACCOUNT_NAME"
az cognitiveservices account create \
  -n $COGNITIVE_ACCOUNT_NAME \
  -g $COGNITIVE_RESOURCE_GROUP \
  --kind ComputerVision \
  --sku S1 \
  -l $REGION \
  --yes
```

Then, Get Computer Vision API Key and endpoint. You'll use the values in later step:
```bash
COMPUTER_VISION_API_ENDPOINT=$(az cognitiveservices account show -n $COGNITIVE_ACCOUNT_NAME -g $COGNITIVE_RESOURCE_GROUP --output tsv |awk '{print $1}')
COMPUTER_VISION_API_KEY=$(az cognitiveservices account keys list -n $COGNITIVE_ACCOUNT_NAME -g $COGNITIVE_RESOURCE_GROUP --output tsv |awk '{print $1}')
echo "API Endpoint: $COMPUTER_VISION_API_ENDPOINT"
echo "API KEY: $COMPUTER_VISION_API_KEY"
```

### Create Blob Storage account & Container

Create an Azure Storage Account
```bash
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
    ComputerVisionSubscription=$COMPUTER_VISION_API_KEY \
    ComputerVisionApiEndpoint=$COMPUTER_VISION_API_ENDPOINT \
    MyStorageConnectionString=$FUNCTION_STORAGE_CONNECTION \
    MyCosmosDBConnectionString=$COSMOS_DB_CONNECTION
```

## Test Request

### HTTP Request body format
HTTP Request body must include the following parameters:
```
{
    'permission': '<Signed permission for shared access signature (Required)>',
    'container': '<Container name to access (Required)>',
    'blobname': '<Blob object name to access (Optional)>'
    'ttl': '<Token time to live period in hours. 1hour by default (Optional)>'
}
```

The following values can be used for permissions:
`a` (Add), `r` (Read), `w` (Write), `d` (Delete), `l` (List)
Concatenate multiple permissions, such as `rwa` = Read, Write, Add

Sample Request Body
```
 {
    'permission': "rl",
    'container': "functiontest",
    'blobname': "sample.png"
    'ttl': 2
 }
```

## Response body format
HTTP response body format is:
```
{
    'token': '<Shared Access Signature Token string>',
    'url' :  '<SAS resource URI>'
}
```

Sample Response Body
```
{'url': 'https://testfunction.blob.core.windows.net/functiontest/yokawasa.png?sig=sXBjML1Fpk9UnTBtajo05ZTFSk0LWFGvARZ6WlVcAog%3D&srt=o&ss=b&spr=https&sp=rl&sv=2016-05-31&se=2017-07-01T00%3A21%3A38Z&st=2017-07-01T23%3A16%3A38Z', 'token': 'sig=sXBjML1Fpk9UnTBtajo05ZTFSk0LWFGvARZ6WlVcAog%3D&srt=o&ss=b&spr=https&sp=rl&sv=2016-05-31&se=2017-07-01T00%3A21%3A38Z&st=2017-07-01T23%3A16%3A38Z'}
```