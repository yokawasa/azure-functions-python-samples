# azure-functions-python-samples
Azure Functions Python Sample Codes

![](https://github.com/yokawasa/azure-functions-python-samples/raw/master/img/azure-function-x-python.png)

```
git clone https://github.com/yokawasa/azure-functions-python-samples.git
cd azure-functions-python-samples
```

## Note
Sample codes are Python2 compatible by default as default Python platform version that Azure Functions support is Python 2.7.X (as of July 1st, 2017). Some of the samples in the project also support Python 3.X. Please see the table below for supporting Python version of each sample.
```
print ("Python Version = '{0}'".format(platform.python_version()))
# >>>2017-07-01T05:33:36.202 Python Version = '2.7.8'
```

## Samples

| Sample | Description | Trigger | In/Out Bindings | Python Ver
| ------------- | ------------- | ------------- | ----------- | ----------- |
| [cosmosdb-trigger-cosmosdb-in-binding](cosmosdb-trigger-cosmosdb-in-binding) | Azure Functions CosmosDB Trigger Python Sample. The function simply read & dump documets which are added to or changed in Azure Cosmos DB by leveraging CosmosDB input binding | CosmosDB | in:DocumentDB | 2.7 |
| [blob-trigger-blob-in-out-bindings](blob-trigger-blob-in-out-bindings) | Azure Functions Blob Trigger Python Sample that simply read file from Azure Blob Storage and write an output file to Azure Blob Storage using Blob Storage input and output bindings respectively | Blob | in:Blob, out:Blob | 2.7 |
| [queue-trigger-rssfeed-crawler](queue-trigger-rssfeed-crawler) | Azure Functions Queue Trigger Python Sample that get RSS feed URL from Queue and dump all items that obtained from RSS feed| Queue | NONE | 2.7 |
| [queue-trigger-tagging-images](queue-trigger-tagging-images) | Azure Functions Queue Trigger Python Sample that tags images stored on Azure Blob Storage by using Cognitive Vision API | Queue | NONE | 2.7 |
| [queue-trigger-sendgrid](queue-trigger-sendgrid) | Azure Functions Queue Trigger Python Sample that send email by using SendGrid bindings | Queue | out:SendGrid | 2.7 |
| [queue-trigger-cosmosdb-in-binding](queue-trigger-cosmosdb-in-binding) | Azure Functions Queue Trigger that obtains a document ID from Queue as a queue message, select a document object from Cosmos DB by using the document ID, and finally dump the object | Queue | in:DocumentDB | 2.7, 3.X |
| [http-trigger-dump-request](http-trigger-dump-request) | Azure Functions HTTP Trigger Python Sample that get and dump HTTPS request info that the trigger receives | HTTP | out:HTTP | 2.7 |
| [blob-sas-token-generator](blob-sas-token-generator)  | Azure Function HTTP Trigger Python Sample that returns a SAS token for Azure Storage for the specified container and blob name | HTTP | out:HTTP | 2.7 |
| [timer-trigger-azuresearch-index-monitoring](timer-trigger-azuresearch-index-monitoring) | Azure Functions Timer Trigger Python Sample that get Azure Search index statistics via API and store the results into DocumentDB | Timer | out:DocumentDB | 2.7 |
| [eventhub-trigger-table-out-bindings](eventhub-trigger-table-out-bindings) | Azure Functions EventHub Trigger Python Sample that read message (device info) in EventHub that sent from sender and write an output record to Azure Table Storage using Table bindings | EventHub | out:Table | 2.7 |
| [proxies-simple-condition-matches](proxies-simple-condition-matches) | Azure Functions Python Sample that re-write dynamic and static page url using Azure Functions Proxies | HTTP | out:HTTP | 2.7 |

## Documents
* [Create a first Python Function in the Azure portal](docs/create-function-app-in-azure-portal.md)
* [How to change the Python version being used in a Function App](docs/custom-python-version.md)

## Tips

* [Running Python Code on Azure Functions App](https://prmadi.com/running-python-code-on-azure-functions-app/)
* [Work with Azure Functions Proxies](https://docs.microsoft.com/en-us/azure/azure-functions/functions-proxies)
* [Create a function triggered by Azure Blob storage](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-storage-blob-triggered-function)
* [Create a function triggered by Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-cosmos-db-triggered-function)

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/yokawasa/azure-functions-python-samples
