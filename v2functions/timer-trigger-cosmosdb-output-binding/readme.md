# timer-trigger-cosmosdb-output-binding (Python)

| Sample | Description | Trigger | In Bindings | Out Bindings
| ------------- | ------------- | ------------- | ----------- | ----------- |
| `timer-trigger-cosmos-output-binding` | Azure Functions Timer Trigger Python Sample. The function gets blog RSS feed and store the results into CosmosDB using Cosmos DB output binding | Timer | NONE | CosmosDB |

## How it works

For a `TimerTrigger` to work, you provide a schedule in the form of a [cron expression](https://en.wikipedia.org/wiki/Cron#CRON_expression)(See the link for full details). A cron expression is a string with 6 separate expressions which represent a given schedule via patterns. The pattern used in this sample (`0 1 * * * *`) is to represent "once a day at 1:00 am". The following is Cron schedule pattern samples:

```txt
# every 5 minutes
0 */5 * * * *

# Run every 6 hours at 10 mins past the hour
10 */6 * * * *

# Run at 1:00 am
0 1 * * * *

# Run at 5:31 pm:
31 17 * * * *
```

## Configurations
As specified in `functions.json`, you need Azure Cosmos DB account for storing data using Cosmos DB output binding

```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "name": "mytimer",
      "type": "timerTrigger",
      "direction": "in",
      "schedule": "0 1 * * * *"
    },
    {
      "direction": "out",
      "type": "cosmosDB",
      "name": "outdoc",
      "databaseName": "testdb",
      "collectionName": "feedcol",
      "leaseCollectionName": "leases",
      "createLeaseCollectionIfNotExists": true,
      "connectionStringSetting": "MyCosmosDBConnectionString",
      "createIfNotExists": true
    }
  ]
}
```

### Create Cosmos DB Account and DB & Collection for testing

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
az cosmosdb database create \
    --name $COSMOSDB_ACCOUNT_NAME \
    --db-name $DATABASE_NAME \
    --key $COSMOSDB_KEY \
    --resource-group $RESOURCE_GROUP

# Create a container with a partition key and provision 400 RU/s throughput.
COLLECTION_NAME="feedcol"
az cosmosdb collection create \
    --resource-group $RESOURCE_GROUP \
    --collection-name $COLLECTION_NAME \
    --name $COSMOSDB_ACCOUNT_NAME \
    --db-name $DATABASE_NAME \
    --partition-key-path /title \
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
COSMOS_DB_CONNECTION="***************"
az webapp config appsettings set \
  -n $FUNCTION_APP_NAME \
  -g $RESOURCE_GROUP \
  --settings \
    MyCosmosDBConnectionString=$COSMOS_DB_CONNECTION
```

### Sample output data stored in CosmosDB

If all goes successfully and feed results are stored in the Cosmos DB that you've created, you'll see the document like this:

```
{
    "items": [
        {
            "id": "dbe7a29c0de2807a5f17e9a3a63bc5f3378bc815",
            "title": "Blog: Update on Volume Snapshot Alpha for Kubernetes",
            "date": "Thu, 17 Jan 2019 00:00:00 +0000"
        },
        {
            "id": "9eda61a9ba684f1acb9a03c8b709f51df80c905a",
            "title": "Blog: Container Storage Interface (CSI) for Kubernetes GA",
            "date": "Tue, 15 Jan 2019 00:00:00 +0000"
        },
        {
            "id": "6c24aea9a7d60f8697c3cfe5328e1c86196facbc",
            "title": "Blog: APIServer dry-run and kubectl diff",
            "date": "Mon, 14 Jan 2019 00:00:00 +0000"
        },
        {
            "id": "00c9181702e3e237bb150d248ffcc27796f8774f",
            "title": "Blog: Kubernetes Federation Evolution",
            "date": "Wed, 12 Dec 2018 00:00:00 +0000"
        },
        {
            "id": "fe818ab1fb07e0a95e2a0e7bf754c15ab95bf6b8",
            "title": "Blog: etcd: Current status and future roadmap",
            "date": "Tue, 11 Dec 2018 00:00:00 +0000"
        }
    ],
    "id": "ab8f4110-0692-4875-9d0f-b864cca603c6",
    "_rid": "dCoKAPwUdioBAAAAAAAAAA==",
    "_self": "dbs/dCoKAA==/colls/dCoKAPwUdio=/docs/dCoKAPwUdioBAAAAAAAAAA==/",
    "_etag": "\"0d004e82-0000-0000-0000-5c544bf70000\"",
    "_attachments": "attachments/",
    "_ts": 1549028343
}
```
