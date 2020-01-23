# azure-functions-python-samples
Azure Functions Python Sample Codes

![](https://github.com/yokawasa/azure-functions-python-samples/raw/master/img/azure-function-x-python.png)

Table of Contents
- [azure-functions-python-samples](#azure-functions-python-samples)
  - [Python functions on Azure Functions 2.X (Public Preview)](#python-functions-on-azure-functions-2x-public-preview)
    - [Samples](#samples)
    - [Documents](#documents)
  - [Python functions on Azure Functions 1.X (Experimental)](#python-functions-on-azure-functions-1x-experimental)
  - [Contributing](#contributing)


## Python functions on Azure Functions 2.X (Public Preview)

This is a collection of Python function samples on Azure Functions 2.X. For a comprehensive development and debugging experience, use the [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python) or [VS Code extension](https://code.visualstudio.com/tutorials/functions-extension/getting-started).

### Samples
| Sample | Description | Trigger | In Bindings | Out Bindings
| ------------- | ------------- | ------------- | ----------- | ----------- |
| [cosmosdb-trigger-cosmosdb-in-binding](v2functions/blob-trigger-cosmosdb-out-binding) | Azure Functions Blob Storage Trigger Python Sample. The function gets image data from Azure Blob Trigger, gets tags for the image with [Computer Vision API](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) ([Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/)), and store the tags into Azure Cosmos DB by leveraging Cosmos DB output binding | Blob Storage | NONE | CosmosDB |
| [cosmos-trigger-cosmodb-output-binding](v2functions/cosmos-trigger-cosmodb-output-binding) | Azure Functions Cosmos DB Trigger Python Sample. The function gets document data from Azure Cosmos DB Trigger, ROT13 encodes obtained clear text, and store encoded data into Azure Cosmos DB by using Cosmos DB output binding | CosmosDB | NONE | CosmosDB |
| [queue-trigger-blob-in-out-binding](v2functions/queue-trigger-blob-in-out-binding) | Azure Functions Queue Trigger Python Sample. The function gets a file name from queue message, reads a blob file named the file name using Blob Input Binding, then ROT13 encodes the obtained clear text, and finally stores it into Azure Blob Storage using Blob Output Binding  | Queue Storage | Blob Storage | Blob Storage |
| [timer-trigger-cosmos-output-binding](v2functions/timer-trigger-cosmosdb-output-binding) | Azure Functions Timer Trigger Python Sample. The function gets blog RSS feed and store the results into CosmosDB using Cosmos DB output binding | Timer | NONE | CosmosDB |
| [http-trigger-blob-sas-token](v2functions/http-trigger-blob-sas-token) | Azure Function HTTP Trigger Python Sample that returns a SAS token for Azure Storage for the specified container and blob name | HTTP | NONE | HTTP |
| [http-trigger-dump-request](v2functions/http-trigger-dump-request) | Azure Function HTTP Trigger Python Sample that returns request dump info with JSON format | HTTP | NONE | HTTP |
| [http-trigger-onnx-model](v2functions/http-trigger-onnx-model) | This function demonstrates running an inference using an ONNX model. It is triggered by an HTTP request. | HTTP | NONE | HTTP |
| [blob-trigger-watermark-blob-out-binding](v2functions/blob-trigger-watermark-blob-out-binding) | Azure Function Python Sample that watermarks an image. This function triggers on an input blob (image) and adds a watermark by calling into the Pillow library. The resulting composite image is then written back to blob storage using a blob output binding. | Blob Storage | Blob Storage | Blob Storage |
| [sbqueue-trigger-sbqueue-out-binding](v2functions/sbqueue-trigger-sbqueue-out-binding) | Azure Functions Service Bus Queue Trigger Python Sample. The function demonstrates reading from a Service Bus queue and placing a message into an output Service Bus queue. | Service Bus Queue | None | Service Bus Queue |

### Documents
* [Quickstart V2 Python Functions with Azure Functions Core Tools](docs/quickstart-v2-python-functions.md)
* [Quickstart Function Samples as a Custom image with Docker](docs/quickstart-samples-custom-image-with-docker.md)
* [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
* [Zip push deployment for Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/deployment-zip-push)
* [Work with Azure Functions Proxies](https://docs.microsoft.com/en-us/azure/azure-functions/functions-proxies)
* [Create a function triggered by Azure Blob storage](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-storage-blob-triggered-function)
* [Create a function triggered by Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-cosmos-db-triggered-function)

---
## Python functions on Azure Functions 1.X (Experimental)

**IMPORTANT**
 - **By default, function apps created in the Azure portal are set to version 2.x. When possible, you should use this runtime version, where new feature investments are being made. Please see [this](https://docs.microsoft.com/en-us/azure/azure-functions/functions-versions) for more detail on Azure Function runtime versions and supported languages.**
 - **Please consider to use 2.X Python funciton as Python function in Azure function 1.X is experimental and new feature investments won't be added to 1.X Python function.**

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

## Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/yokawasa/azure-functions-python-samples
