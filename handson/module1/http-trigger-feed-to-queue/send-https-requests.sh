#!/bin/sh

#api_url="AZURE_FUNCTION_URL ex https://<app_account>.azurewebsites.net/api/<func_name>?code=xxxxx"
api_url="https://yoichikademo27.azurewebsites.net/api/http-trigger-feed-to-queue?code=dTtNrLDYaaOrF3Gl6lkZfPRMB7Z9I47wYyJhCUWbvnHrzgOUJTp2dw=="

echo "Sending HTTP POST Request............."
curl -s\
 -H "Content-Type: application/json; charset=UTF-8"\
 -XPOST ${api_url} -d'{
    "feedurl": "https://azure.microsoft.com/en-us/blog/feed/"
}'

echo ""
