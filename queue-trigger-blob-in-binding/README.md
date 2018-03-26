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

Here is how the functions works when send a queue message `sample.txt` 
1. It is triggered to start the function when a new message is detected in a queue named `myqueue4python`. 
2. Obtain the queue message (= blob file name) when the function is triggered by Queue trigger.
3. Using Blob storage input binding, read a blob file named `sample.txt` (path: `inputcontainer4funcs/sample.txt`) which is exactly the same as the message you sent in the queue, and assign the content into clear_text variable
4. Encrypt the content in clear_text variable using ROT13 encyrption and assign the encrypted content into encrypted_text variable


## LINKS
- [Azure Blob storage bindings for Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob)