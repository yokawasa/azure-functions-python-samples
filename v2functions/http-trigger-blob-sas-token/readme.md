# http-trigger-blob-sas-token (Python)

- [http-trigger-blob-sas-token (Python)](#http-trigger-blob-sas-token-python)
  - [Configuration](#configuration)
  - [How to develop and publish the function](#how-to-develop-and-publish-the-function)
    - [Local development](#local-development)
    - [Publish the function to the cloud](#publish-the-function-to-the-cloud)
  - [API Format](#api-format)
    - [HTTP Request body format](#http-request-body-format)
    - [Response body format](#response-body-format)
  - [Examples](#examples)
    - [Get SAS Token to access blob files in Azure Blob Storage](#get-sas-token-to-access-blob-files-in-azure-blob-storage)
    - [Uploading files to Azure Blob Storage](#uploading-files-to-azure-blob-storage)

| Sample | Description | Trigger | In Bindings | Out Bindings
| ------------- | ------------- | ------------- | ----------- | ----------- |
| `http-trigger-blob-sas-token` | Azure Function HTTP Trigger Python Sample that returns a SAS token for Azure Storage for the specified container and blob name | HTTP | NONE | HTTP |

## Configuration

You need Azure Storage account for which you want the function to generate SAS token for specified container and blob name.

Create an Azure Storage Account
```sh
RESOURCE_GROUP="rg-testfunctions"
REGION="japaneast"
STORAGE_ACCOUNT="teststore"
az storage account create --name $STORAGE_ACCOUNT \
    --location $REGION \
    --resource-group $RESOURCE_GROUP \
    --sku Standard_LRS
```

Create a container in the storage you've created
```sh
# Get Storage Key
ACCESS_KEY=$(az storage account keys list --account-name $STORAGE_ACCOUNT --resource-group $RESOURCE_GROUP --output tsv |head -1 | awk '{print $3}')

az storage container create  \
    --name "functiontest" \
    --account-name $STORAGE_ACCOUNT \
    --account-key $ACCESS_KEY
```

## How to develop and publish the function
### Local development
```sh
func host start
```

### Publish the function to the cloud

Publish the function to the cloud
```sh
FUNCTION_APP_NAME="MyFunctionApp"
func azure functionapp publish $FUNCTION_APP_NAME --build-native-deps --no-bundler
```

Add Functions App Settings
```sh
FUNCTION_STORAGE_CONNECTION="*************"
az webapp config appsettings set \
  -n $FUNCTION_APP_NAME \
  -g $RESOURCE_GROUP \
  --settings \
    MyStorageConnectionString=$FUNCTION_STORAGE_CONNECTION 
```

## API Format

### HTTP Request body format
HTTP Request body must include the following parameters:
```
{
    'permission': '<Signed permission for shared access signature (Required)>',
    'container': '<Container name to access (Required)>',
    'blobname': '<Blob object name to access (Optional)>'
    'ttl': '<Token time to live period in hours. 1hour by default (Optional)>'
}
```

The following values can be used for permissions:
`a` (Add), `r` (Read), `w` (Write), `d` (Delete), `l` (List)
Concatenate multiple permissions, such as `rwa` = Read, Write, Add

Sample Request Body
```
 {
    'permission': "rl",
    'container': "functiontest",
    'blobname': "sample.png"
    'ttl': 2
 }
```

### Response body format
HTTP response body format is:
```
{
    'token': '<Shared Access Signature Token string>',
    'url' :  '<SAS resource URI>'
}
```

Sample Response Body
```
{"token": "sv=2018-03-28&ss=b&srt=o&sp=rl&se=2019-03-29T14%3A02%3A37Z&st=2019-03-29T11%3A57%3A37Z&spr=https&sig=Sh7RAa5MZBk7gfv0haCbEbllFXoiOWJDK9itzPeqURE%3D", "url": "https://MyFunctionApp.blob.core.windows.net/functiontest/sample.jpg?sv=2018-03-28&ss=b&srt=o&sp=rl&se=2019-03-29T14%3A02%3A37Z&st=2019-03-29T11%3A57%3A37Z&spr=https&sig=Sh7RAa5MZBk7gfv0haCbEbllFXoiOWJDK9itzPeqURE%3D" }
```

## Examples
### Get SAS Token to access blob files in Azure Blob Storage

There is a test request command - `scripts/send-test-blob-sas-token.sh`
```sh
api_url="AZURE_FUNCTION_ENDPOINT: ex. https://<app_account>.azurewebsites.net/api/<func_name>"
api_key="AZURE_FUNCTION_KEY: ex. aRVQ7Lj0vzDhY0JBYF8gpxYyEBxLwhO51JSC7X5dZFbTvROs7xNg=="

echo "Sending HTTP POST Request............."
curl -s\
 -H "Content-Type: application/json; charset=UTF-8"\
 -H "x-functions-key: ${api_key}"\
 -XPOST ${api_url} -d'{
    "permission": "rl",
    "container": "functiontest",
    "blobname": "sample.png",
    "ttl": 1
}'
```

Replace `api_url` and `api_key` with your values in the script and execute it. You'll get response back like this:

```json
{
    "token": "sv=2018-03-28&ss=b&srt=o&sp=rl&se=2019-03-31T05%3A17%3A11Z&st=2019-03-31T03%3A12%3A11Z&spr=https&sig=A99ZFhDK2fwHnYl5Nd1dm%2Bcd1xJbolHz5wZLG9ewOvs%3D",
    "url": "https://MyFunctionApp.blob.core.windows.net/functiontest/sample.jpg?sv=2018-03-28&ss=b&srt=o&sp=rl&se=2019-03-31T05%3A17%3A11Z&st=2019-03-31T03%3A12%3A11Z&spr=https&sig=A99ZFhDK2fwHnYl5Nd1dm%2Bcd1xJbolHz5wZLG9ewOvs%3D"
}
```

You can access to the blob with `url` that is included in the response body

```sh
$ open https://MyFunctionApp.blob.core.windows.net/functiontest/sample.jpg?sv=2018-03-28&ss=b&srt=o&sp=rl&se=2019-03-31T05%3A17%3A11Z&st=2019-03-31T03%3A12%3A11Z&spr=https&sig=A99ZFhDK2fwHnYl5Nd1dm%2Bcd1xJbolHz5wZLG9ewOvs%3D
```

### Uploading files to Azure Blob Storage

Here is an example of uploading files to Azure Blob Storage using the http-trigger-blob-sas-token function.

> [scripts/upload-blob-sas-token.py](../../scripts/upload-blob-sas-token.py)

```python
import sys
import os
import ntpath
import json 
import requests

_AZFUNC_API_KEY="AZURE_FUNCTION_KEY: ex. aRVQ7Lj0vzDhY0JBYF8gpxYyEBxLwhO51JSC7X5dZFbTvROs7xNg=="
_AZFUNC_API_URL="AZURE_FUNCTION_ENDPOINT: ex. https://<app_account>.azurewebsites.net/api/<func_name>"

if __name__ == '__main__':
    
    file_path = "/tmp/test.jpg"
    content_type = "image/jpeg"
    container_name = "functiontest"

    file_name = ntpath.basename(file_path)

    ### Getting SAS token for uploading files to Azure Blob Storage
    payload = {
        "permission": "awl",
        "container": container_name,
        "blobname": file_name
    }
    r = requests.post(_AZFUNC_API_URL,
            headers = {
                "Content-Type" : "application/json; charset=UTF-8",
                "x-functions-key": _AZFUNC_API_KEY
            },
            data=json.dumps(payload)
        )
    if r.status_code != 200:
        print(f"Getting SAS token request result: status code={r.status_code}")
        sys.exit(1) 

    content_dict = json.loads(r.content.decode())
    url = content_dict['url'] 

    ### Uploading files to Azure Blob Storage
    with open(file_path , 'rb') as filehandle:
        r = requests.put(url,
                data=filehandle,
                headers={
                    'Content-Type': content_type,
                    'x-ms-blob-type': 'BlockBlob'
                },
                params={
                    'file': file_path
                }
            )
        print(f"Uploading request result: status code={r.status_code}")
```

In the example above, you will upload `/tmp/test.jpg` to a container named `functiontest` in your Azure Blob Storage.
