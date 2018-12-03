# cosmosdb-trigger-cosmosdb-in-binding
Azure Functions CosmosDB Trigger Python Sample. The function simply read & dump documets which are added to or changed in Azure Cosmos DB by leveraging CosmosDB input binding



## Configuration - function.json

```
{
  "bindings": [
    {
      "type": "cosmosDBTrigger",
      "name": "triggeredCosmosdb",
      "connectionStringSetting": "yoichikademo1_DOCUMENTDB",
      "databaseName": "mydb",
      "collectionName": "mycontent",
      "leaseCollectionName": "mycontent_leaves",
      "createLeaseCollectionIfNotExists": true,
      "direction": "in"
    },
    {
      "type": "documentDB",
      "name": "inputCosmosdb",
      "databaseName": "mydb",
      "collectionName": "mycontent",
      "connection": "yoichikademo1_DOCUMENTDB",
      "direction": "in"
    }
  ],
  "disabled": false
}
```

[NOTE] Currently all documents in the collection are returned.
