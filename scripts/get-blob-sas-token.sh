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
    "blobname": "sample.jpg",
    "ttl": 1
}'
echo ""
