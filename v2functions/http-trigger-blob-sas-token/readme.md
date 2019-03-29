
# http-trigger-blob-sas-token (Python)

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

## Sending Test Requests

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

### Sending requests with test command

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
    "ttl": 2
}'
```

Replace `api_url` and `api_key` with your values in the script and execute it. You'll get response back like this:

```json
{
    "status": 200,
    "body": "{\"token\": \"sv=2018-03-28&ss=b&srt=o&sp=rl&se=2019-03-29T14%3A50%3A46Z&st=2019-03-29T12%3A45%3A46Z&spr=https&sig=%2FS7Z0qnrk3UvyeXZtb4ZbqjTCORnRqkEE3e1O6Gb1KA%3D\", \"url\": \"https://MyFunctionApp.blob.core.windows.net/functiontest/sample.jpg?sv=2018-03-28&ss=b&srt=o&sp=rl&se=2019-03-29T14%3A50%3A46Z&st=2019-03-29T12%3A45%3A46Z&spr=https&sig=%2FS7Z0qnrk3UvyeXZtb4ZbqjTCORnRqkEE3e1O6Gb1KA%3D\"}",
    "headers": {"Content-Type": "application/json"}
}
```

You can access to the blob with `url` that is included in the response body

```sh
open https://MyFunctionApp.blob.core.windows.net/functiontest/sample.jpg?sv=2018-03-28&ss=b&srt=o&sp=rl&se=2019-03-29T14%3A50%3A46Z&st=2019-03-29T12%3A45%3A46Z&spr=https&sig=%2FS7Z0qnrk3UvyeXZtb4ZbqjTCORnRqkEE3e1O6Gb1KA%3D
```