# azure-functions-python-samples
Azure Functions Python Sample Codes

```
git clone https://github.com/yokawasa/azure-functions-python-samples.git
cd azure-functions-python-samples
```

## Note
Sample codes are Python2 compatible, not Python3 as default Python platform version that Azure Functions support is Python 2.7.X (as of July 1st, 2017)
```
print ("Python Version = '{0}'".format(platform.python_version()))
# >>>2017-07-01T05:33:36.202 Python Version = '2.7.8'
```

## Samples

Sample Type | Description | Code
------------ | ------------- | :-----------: |
Blob Trigger | Azure Functions Blob Trigger Python Sample that simply read file from Azure Blob Storage and write an output file to Azure Blob Storage | [blob-trigger-read-write-blob](https://github.com/yokawasa/azure-functions-python-samples/tree/master/blob-trigger-read-write-blob) |
Queue Trigger | Azure Functions Queue Trigger Python Sample that get RSS feed URL from Queue and dump all items that obtained from RSS feed| [queue-trigger-rssfeed-crawler](https://github.com/yokawasa/azure-functions-python-samples/tree/master/queue-trigger-rssfeed-crawler) |
Queue Trigger | Azure Functions Queue Trigger Python Sample that tags images stored on Azure Blob Storage by using Cognitive Vision API | [queue-trigger-tagging-images](https://github.com/yokawasa/azure-functions-python-samples/tree/master/queue-trigger-tagging-images) |
HTTP Trigger | Azure Functions HTTP Trigger Python Sample that get and dump HTTPS request info that the trigger receives | [http-trigger-dump-request](https://github.com/yokawasa/azure-functions-python-samples/tree/master/http-trigger-dump-request) |
HTTP Trigger | Azure Function HTTP Trigger Python Sample that returns a SAS token for Azure Storage for the specified container and blob name | [blob-sas-token-generator](https://github.com/yokawasa/azure-functions-python-samples/tree/master/blob-sas-token-generator) |
Timer Trigger | Azure Functions Timer Trigger Python Sample that get Azure Search index statistics via API and store the results into DocumentDB | [timer-trigger-azuresearch-index-monitoring](https://github.com/yokawasa/azure-functions-python-samples/tree/master/timer-trigger-azuresearch-index-monitoring) |
