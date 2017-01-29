#!/bin/sh

api_url="https://yoichikademo1.azurewebsites.net/api/HttpTrigger-Python-Custom?code=O95zka81NsaDmNCXzyCe9/t7g6H1GwgoJgAdsGS3Slp3K3cHMDfalA=="
api_key="O95zka81NsaDmNCXzyCe9/t7g6H1GwgoJgAdsGS3Slp3K3cHMDfalA=="

echo "Sending HTTP GET Request............."
curl -s\
 -H "Content-Type: application/json; charset=UTF-8"\
 -H "api-key: ${api_key}"\
 -XGET ${api_url} -d'foo=abc1111&bar=xyz2222'

echo "Sending HTTP POST Request............."
curl -s\
 -H "Content-Type: application/json; charset=UTF-8"\
 -H "api-key: ${api_key}"\
 -XPOST ${api_url} -d'{
    "id: "00000121",
    "name": "Yoichi Kawasaki"
}'
