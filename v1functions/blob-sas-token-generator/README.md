# blob-sas-token-generator
An HTTP trigger Azure Function that returns a SAS token for Azure Storage for the specified container and blob name. You can also specify access permissions for the container/blob name and optionally its token time-to-live period. The SAS token expires in an hour by default.

## HTTP Request body format
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
"a" (Add), "r" (Read), "w" (Write), "d" (Delete), "l" (List)
Concatenate multiple permissions, such as "rwa" = Read, Write, Add

Sample Request Body
```
 {
    'permission': "rl",
    'container': "functions",
    'blobname': "sample.png"
    'ttl': 2
 }
```

## Response body format
HTTP response body format is:
```
{
    'token': '<Shared Access Signature Token string>',
    'url' :  '<SAS resource URI>'
}
```

Sample Response Body
```
{'url': 'https://testfunction.blob.core.windows.net/functiontest/yokawasa.png?sig=sXBjML1Fpk9UnTBtajo05ZTFSk0LWFGvARZ6WlVcAog%3D&srt=o&ss=b&spr=https&sp=rl&sv=2016-05-31&se=2017-07-01T00%3A21%3A38Z&st=2017-07-01T23%3A16%3A38Z', 'token': 'sig=sXBjML1Fpk9UnTBtajo05ZTFSk0LWFGvARZ6WlVcAog%3D&srt=o&ss=b&spr=https&sp=rl&sv=2016-05-31&se=2017-07-01T00%3A21%3A38Z&st=2017-07-01T23%3A16%3A38Z'}
```

## Test Command

```
#!/bin/sh

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
echo ""
```
