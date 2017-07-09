# azure-functions-python-samples
Azure Functions Python Sample Codes

![](https://github.com/yokawasa/azure-functions-python-samples/raw/master/img/azure-function-x-python.png)

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

| Sample | Description | Type | In/Out Bindings
| ------------- | ------------- | ------------- | ----------- |
| [blob-trigger-read-write-blob](https://github.com/yokawasa/azure-functions-python-samples/tree/master/blob-trigger-read-write-blob) | Azure Functions Blob Trigger Python Sample that simply read file from Azure Blob Storage and write an output file to Azure Blob Storage | Blob Trigger | input:Blob, outout:Blob |
| [queue-trigger-rssfeed-crawler](https://github.com/yokawasa/azure-functions-python-samples/tree/master/queue-trigger-rssfeed-crawler) | Azure Functions Queue Trigger Python Sample that get RSS feed URL from Queue and dump all items that obtained from RSS feed| Queue Trigger | NONE |
| [queue-trigger-tagging-images](https://github.com/yokawasa/azure-functions-python-samples/tree/master/queue-trigger-tagging-images) | Azure Functions Queue Trigger Python Sample that tags images stored on Azure Blob Storage by using Cognitive Vision API | Queue Trigger | NONE |
| [http-trigger-dump-request](https://github.com/yokawasa/azure-functions-python-samples/tree/master/http-trigger-dump-request) | Azure Functions HTTP Trigger Python Sample that get and dump HTTPS request info that the trigger receives | HTTP Trigger | output:HTTP |
| [blob-sas-token-generator](https://github.com/yokawasa/azure-functions-python-samples/tree/master/blob-sas-token-generator)  | Azure Function HTTP Trigger Python Sample that returns a SAS token for Azure Storage for the specified container and blob name | HTTP Trigger | output:HTTP |
| [timer-trigger-azuresearch-index-monitoring](https://github.com/yokawasa/azure-functions-python-samples/tree/master/timer-trigger-azuresearch-index-monitoring) | Azure Functions Timer Trigger Python Sample that get Azure Search index statistics via API and store the results into DocumentDB | Timer Trigger | output:DocumentDB |
| [eventhub-trigger-device-data-write-table](https://github.com/yokawasa/azure-functions-python-samples/tree/master/eventhub-trigger-device-data-write-table) | Azure Functions EventHub Trigger Python Sample that read message (device info) in EventHub that sent from sender and write an output record to Azure Table Storage | EventHub Trigger | output:Table |


## Tips

* [Running Python Code on Azure Functions App](https://prmadi.com/running-python-code-on-azure-functions-app/)
* [Using a custom version of Python](://github.com/Azure/azure-webjobs-sdk-script/wiki/Using-a-custom-version-of-Python)

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/yokawasa/azure-functions-python-samples
