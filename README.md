# azure-functions-python-samples
Azure Functions Python Sample Codes

```
git clone https://github.com/yokawasa/azure-functions-python-samples.git
cd azure-functions-python-samples
```

## Samples

Sample Type | Description | Code
------------ | ------------- | :-----------: |
Blob Trigger | Azure Functions Blob Trigger Python Sample that simply read file from Azure Blob Storage and write an output file to Azure Blob Storage | [blob-trigger-read-write-blob](https://github.com/yokawasa/azure-functions-python-samples/tree/master/blob-trigger-read-write-blob) |
Queue Trigger | Azure Functions Queue Trigger Python Sample that get RSS feed URL from Queue and dump all items that obtained from RSS feed| [queue-trigger-rssfeed-crawler](https://github.com/yokawasa/azure-functions-python-samples/tree/master/queue-trigger-rssfeed-crawler) |
Queue Trigger | Azure Functions Queue Trigger Python Sample that tags images stored on Azure Blob Storage by using Cognitive Vision API | [queue-trigger-tagging-images](https://github.com/yokawasa/azure-functions-python-samples/tree/master/queue-trigger-tagging-images) |
HTTP Trigger | Azure Functions HTTP Trigger Python Sample that get and dump HTTPS request info that the trigger receives | [http-trigger-dump-request](https://github.com/yokawasa/azure-functions-python-samples/tree/master/http-trigger-dump-request) |
Timer Trigger | Azure Functions Timer Trigger Python Sample that get Azure Search index statistics via API and store the results into DocumentDB | [timer-trigger-azuresearch-index-monitoring](https://github.com/yokawasa/azure-functions-python-samples/tree/master/timer-trigger-azuresearch-index-monitoring) |
