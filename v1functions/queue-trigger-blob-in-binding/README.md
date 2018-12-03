# queue-trigger-blob-in-binding
Azure Functions Queue Trigger Python Sample that obtain a blog file name from Queue as a queue message and read a file named the blog file name in Azure Blob Storage using Blob Input Binding| Queue

## Prerequisites
- Azure Functions Account
- General-purpose storage account (Blob storage triggers require a general-purpose storage account)

## Trigger and Input/Output Binding (function.json)

```
{
  "bindings": [
    {
      "name": "inputMessage",
      "type": "queueTrigger",
      "direction": "in",
      "queueName": "myqueue4python",
      "connection": "yourstorageaccount_STORAGE"
    },
    {
      "type": "blob",
      "name": "inputBlob",
      "path": "inputcontainer4funcs/{queueTrigger}",
      "connection": "yourstorageaccount_STORAGE",
      "direction": "in"
    }
  ],
  "disabled": false
}
```

## How the function works?

Here is how the functions works when you add a queue message `sample.txt` in queue named `myqueue4python`. Queue message is supposed to be a blob file name.
1. The function is triggered to start when a new message is detected in the queue named `myqueue4python`. 
2. By reading an environment variable named `inputMessage`, the function gets a file name (full path) in which the blob file name is written. The function get the blob file name (=`sample.txt`) from reading the file. 
3. Using Blob storage input binding, the function reads the blob file named `sample.txt` (path: `inputcontainer4funcs/sample.txt`) and assign the content into clear_text variable
4. The function encrypts the content in clear_text variable using ROT13 encyrption and assign the encrypted content into encrypted_text variable


## LINKS
- [Azure Blob storage bindings for Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob)