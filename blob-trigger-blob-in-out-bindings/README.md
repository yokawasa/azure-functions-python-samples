# blob-trigger-blob-in-out-bindings
Azure Functions Blob Trigger Python Sample that simply read file from Azure Blob Storage and write an output file to Azure Blob Storage using Blob Storage input and output bindings respectively

## Prerequisites
- Azure Functions Account
- General-purpose storage account (Blob storage triggers require a general-purpose storage account)

## Trigger and Input/Output Binding (function.json)

```
{
  "bindings": [
    {
      "name": "blobTriggerTest",
      "type": "blobTrigger",
      "direction": "in",
      "path": "inputcontainer4funcs/{blobname}.{blobextension}",
      "connection": "yourstorageaccount_STORAGE"
    },
    {
      "type": "blob",
      "name": "inputBlob",
      "path": "inputcontainer4funcs/{blobname}.{blobextension}",
      "direction": "in",
      "connection": "yourstorageaccount_STORAGE"
    },
    {
      "type": "blob",
      "name": "outputBlob",
      "path": "outputcontainer4funcs/{blobname}-encoded.{blobextension}",
      "direction": "out",
      "connection": "yourstorageaccount_STORAGE"
    }
  ],
  "disabled": false
}
```

You can specify an exact file name, for example, `clear.txt if you want Blob trigger to start the function only when the file is uploaded like this:
```
    {
      "type": "blob",
      "name": "inputBlob",
      "path": "inputcontainer4funcs/clear.txt",
      "direction": "in",
      "connection": "yourstorageaccount_STORAGE"
    },
```

## How the function works?

Here is how the functions works when you upload a blob file named `sample.txt`
1. The function is triggered to start when a new or updated blob is detected in a container named `inputcontainer4funcs`
2. The function reads the detected blob file using Blob storage input binding, and assigns the content into clear_text variable
3. The function encrypts the content in clear_text variable using ROT13 encyrption and assign the encrypted content into encrypted_text variable
4. The function stores the encrypted content into a file named `{blobname}-encoded.{blobextension}` in a container named `outputcontainer4funcs`

[NOTE] In python code, you can NOT get the blob name in the Blob Trigger function. Use another mechanism to trigger the blob processing, such as a queue message that contains the blob name. See the blob input bindings example in [this page](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob#input---example) for more detail. 

Seel Also a sample where you can get the blob file name using queue trigger - [queue-trigger-blob-in-bindings](../queue-trigger-blob-in-binding/)


## LINKS
- [Azure Blob storage bindings for Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob)