#!/bin/sh

# api_url="AZURE_FUNCTION_ENDPOINT: ex. https://<app_account>.azurewebsites.net/api/<func_name>"
# api_key="AZURE_FUNCTION_KEY: ex. aRVQ7Lj0vzDhY0JBYF8gpxYyEBxLwhO51JSC7X5dZFbTvROs7xNg=="

# func locally
api_url="http://localhost:7071/api/http-trigger-blob-sas-token"
# Docker
# api_url="http://localhost:8080/api/http-trigger-blob-sas-token"
api_key=""

echo "Sending HTTP POST Request............."
 curl -s\
 -H "Content-Type: application/json; charset=UTF-8"\
 -H "x-functions-key: ${api_key}"\
 -XPOST ${api_url} -d'{
    "permission": "rl",
    "container": "functiontest",
    "blobname": "sample.jpg",
    "ttl": 2
}'
echo ""
