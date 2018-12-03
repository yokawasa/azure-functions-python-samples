#!/bin/sh

api_url="AZURE_FUNCTION_ENDPOINT: ex. https://<app_account>.azurewebsites.net/api/<func_name>"
api_key="AZURE_FUNCTION_KEY: ex. aRVQ7Lj0vzDhY0JBYF8gpxYyEBxLwhO51JSC7X5dZFbTvROs7xNg=="

echo "Sending Bad Request #1: Invalid HTTP Method............."
curl -s\
 -H "Content-Type: application/json; charset=UTF-8"\
 -H "x-functions-key: ${api_key}"\
 -XGET ${api_url} 
echo ""

echo "Sending Bad Request #1: Invalid Request Body............."
curl -s\
 -H "Content-Type: application/json; charset=UTF-8"\
 -H "x-functions-key: ${api_key}"\
 -XPOST ${api_url} -d'{
    "permission": "rl"
}'
echo ""

echo "Sending Bad Request #3: Invalid TTL............."
curl -s\
 -H "Content-Type: application/json; charset=UTF-8"\
 -H "x-functions-key: ${api_key}"\
 -XPOST ${api_url} -d'{
    "permission": "rl",
    "container": "functiontest",
    "blobname": "sample.png",
    "ttl": -1
}'
echo ""




