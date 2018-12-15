# azure-functions-python-samples
Azure Functions Python Sample Codes

![](https://github.com/yokawasa/azure-functions-python-samples/raw/master/img/azure-function-x-python.png)

Table of Contents
- [azure-functions-python-samples](#azure-functions-python-samples)
  - [V2 Functions (Public Preview)](#v2-functions-public-preview)
    - [V2 Functions Samples](#v2-functions-samples)
    - [Documents](#documents)
  - [V1 Functions (Experimental)](#v1-functions-experimental)
    - [V1 Functions Samples](#v1-functions-samples)
    - [Documents (Deprecating)](#documents-deprecating)
  - [Contributing](#contributing)


## V2 Functions (Public Preview)

### V2 Functions Samples
| Sample | Description | Trigger | In Bindings | Out Bindings
| ------------- | ------------- | ------------- | ----------- | ----------- |
| [cosmosdb-trigger-cosmosdb-in-binding](v2functions/blob-trigger-cosmosdb-out-binding) | Azure Functions Blob Storage Trigger Python Sample. The function gets image data from Azure Blob Trigger, gets tags for the image with [Computer Vision API](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) ([Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/)), and store the tags into Azure Cosmos DB by leveraging CosmosDB output binding | Blob Storage | NONE | CosmosDB |

### Documents
* [Quickstart V2 Python Functions](docs/quickstart-v2-python-functions.md)
* [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
* [Zip push deployment for Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/deployment-zip-push)
* [Work with Azure Functions Proxies](https://docs.microsoft.com/en-us/azure/azure-functions/functions-proxies)
* [Create a function triggered by Azure Blob storage](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-storage-blob-triggered-function)
* [Create a function triggered by Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-cosmos-db-triggered-function)

---
## V1 Functions (Experimental)

> [NOTE] V1 Functions sample codes are Python2 compatible by default as default Python  platform version that Azure Functions support is Python 2.7.X (as of July 1st, 2017). Some of the samples in the project also support Python 3.X. Please see the table below for supporting Python version of each sample.
```
print ("Python Version = '{0}'".format(platform.python_version()))
# >>>2017-07-01T05:33:36.202 Python Version = '2.7.8'
```
> For those who want to change the Python runtime version to 3.5/3.6, here is a procedure: 
[How to change the Python version being used in a Function App](docs/custom-python-version.md)

### V1 Functions Samples
| Sample | Description | Trigger | In Bindings | Out Bindings
| ------------- | ------------- | ------------- | ----------- | ----------- |
| [cosmosdb-trigger-cosmosdb-in-binding](v1functions/cosmosdb-trigger-cosmosdb-in-binding) | Azure Functions CosmosDB Trigger Python Sample. The function simply read & dump documets which are added to or changed in Azure Cosmos DB by leveraging CosmosDB input binding | CosmosDB | CosmosDB | NONE |
| [blob-trigger-blob-in-out-bindings](v1functions/blob-trigger-blob-in-out-bindings) | Azure Functions Blob Trigger Python Sample that simply read file from Azure Blob Storage and write an output file to Azure Blob Storage using Blob Storage input and output bindings respectively | Blob Storage | Blob Storage | Blob Storage |
| [queue-trigger-blob-in-bindings](v1functions/queue-trigger-blob-in-binding) | Azure Functions Queue Trigger Python Sample that obtain a blog file name from Queue as a queue message and read a file named the blog file name in Azure Blob Storage using Blob Input Binding| Queue Storage | Blob Storage| NONE |
| [queue-trigger-rssfeed-crawler](v1functions/queue-trigger-rssfeed-crawler) | Azure Functions Queue Trigger Python Sample that get RSS feed URL from Queue and dump all items that obtained from RSS feed| Queue Storage| NONE | NONE |
| [queue-trigger-tagging-images](v1functions/queue-trigger-tagging-images) | Azure Functions Queue Trigger Python Sample that tags images stored on Azure Blob Storage by using Cognitive Vision API | Queue Storage| NONE | NONE |
| [queue-trigger-sendgrid](v1functions/queue-trigger-sendgrid) | Azure Functions Queue Trigger Python Sample that send email by using SendGrid bindings | Queue Storage| NONE | SendGrid |
| [queue-trigger-cosmosdb-in-binding](v1functions/queue-trigger-cosmosdb-in-binding) | Azure Functions Queue Trigger that obtains a document ID from Queue as a queue message, select a document object from Cosmos DB by using the document ID, and finally dump the object | Queue Storage| CosmosDB | NONE |
| [http-trigger-dump-request](v1functions/http-trigger-dump-request) | Azure Functions HTTP Trigger Python Sample that get and dump HTTPS request info that the trigger receives | HTTP | NONE | HTTP |
| [blob-sas-token-generator](v1functions/blob-sas-token-generator)  | Azure Function HTTP Trigger Python Sample that returns a SAS token for Azure Storage for the specified container and blob name | HTTP | NONE | HTTP |
| [timer-trigger-azuresearch-index-monitoring](v1functions/timer-trigger-azuresearch-index-monitoring) | Azure Functions Timer Trigger Python Sample that get Azure Search index statistics via API and store the results into CosmosDB | Timer | NONE | CosmosDB |
| [eventhub-trigger-table-out-bindings](v1functions/eventhub-trigger-table-out-bindings) | Azure Functions EventHub Trigger Python Sample that read message (device info) in EventHub that sent from sender and write an output record to Azure Table Storage using Table bindings | EventHub | NONE | Table Storage|
| [proxies-simple-condition-matches](v1functions/proxies-simple-condition-matches) | Azure Functions Python Sample that re-write dynamic and static page url using Azure Functions Proxies | HTTP | NONE | HTTP |

### Documents (Deprecating)
* [V1: How to change the Python version being used in a Function App](docs/custom-python-version.md)
* [V1: How to install the Python modules](docs/install-python-modules.md)
* [V1: Local Git Deployment to Azure Functions (Japanese only)](docs/local-git-deployment_ja.md)


## Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/yokawasa/azure-functions-python-samples
