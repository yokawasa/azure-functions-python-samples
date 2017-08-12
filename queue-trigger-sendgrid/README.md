# queue-trigger-sendgrid
Azure Functions Queue Trigger Python Sample that send email by using SendGrid bindings

| Trigger | In/Out Bindings |
------------ | ----------- |
| Queue Trigger | output:SendGrid |


## Pre-requisites

 * **SendGrid Account/API Key**: You need an SendGrid account and API Key with which you can use Azure Functions to send customized email programmatically. For more info on SendGrid, please see [How to Send Email Using SendGrid with Azure](https://docs.microsoft.com/en-us/azure/app-service-web/sendgrid-dotnet-how-to-send-email)
 * **Azure Storage Account (General Purpose Type)**: You need an Azure Storage account as the function read message info in Azure Queue Storage

## Bindings Configuration

You need to configure 2 kinds of bindings: (1) Queue Trigger (2) SendGrid output Binding. You can configure them either by directly editing function.json file or via Azure Functions' "Function Apps - Functions - Integrate" UI in Azure Portal

```
{
  "bindings": [
    {
      "type": "queueTrigger",
      "name": "<The name used to identify the trigger data in your code>", 
      "direction": "in",
      "queueName": "<Name of queue to poll>",
      "connection": "<Name of app setting - see (note1)>"
    },
    {
      "type": "sendGrid", 
      "name": "<The name to identify  the request body in your code>",  
      "from": "<The sender's email address>",
      "apiKey": "<Name of app setting for your SendGrid API key>",
      "direction": "out"
    }
  ],
  "disabled": false
}
```

* note1 - The connection property must contain the name of an app setting that contains a storage connection string. In the Azure portal, the standard editor in the Integrate tab configures this app setting for you when you select a storage account.
* App Settings - For detail information about how to work with App Service settings, please refer to [How to manage a function app in the Azure portal](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings)

Here is an example configuration for this sample code:
```
{
  "bindings": [
    {
      "name": "inputMessage",
      "type": "queueTrigger",
      "direction": "in",
      "queueName": "sendgrid-queue",
      "connection": "azurefunctionsb5d4aebe_STORAGE"
    },
    {
      "type": "sendGrid",
      "name": "outputMessage",
      "from": "sender@contoso.com",
      "apiKey": "MY_SENDGRID_API_KEY",
      "direction": "out"
    }
  ],
  "disabled": false
}
```

## How to Test
(1) Deploy run.py and functions.json to your function app
(2) Configure binding file - function.json
(3) Add a message to your queue
(4) Check if the function send an email via SendGrid. 

See also [Strategies for testing your code in Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-test-a-function)


## Useful Links
* [How to Send Email Using SendGrid with Azure](https://docs.microsoft.com/en-us/azure/app-service-web/sendgrid-dotnet-how-to-send-email)
* [How to manage a function app in the Azure portal](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings)
* [Azure Functions SendGrid bindings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-sendgrid)
