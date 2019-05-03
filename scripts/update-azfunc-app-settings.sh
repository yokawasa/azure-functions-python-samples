#!/bin/sh
set -e -x

RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
APP_NAME="<FUNCTION APP NAME>" #  the name needs to be unique across all apps in Azure.
STORAGE_ACCOUNT_NAME="<STORAGE ACCOUNT NAME>"
COSMOSDB_ACCOUNT_NAME="<COSMOSDB ACCOUNT NAME>"
COGNITIVE_ACCOUNT_NAME="<COGNITIVE ACCOUNT NAME>"
COGNITIVE_RESOURCE_GROUP="<COGNITIVE RESOURCE GROUP>"

STORAGE_ACCOUNT_KEY=$(az storage account keys list --account-name $STORAGE_ACCOUNT_NAME --resource-group $RESOURCE_GROUP --output tsv |head -1 | awk '{print $3}')
COSMOSDB_ACCOUNT_KEY=$(az cosmosdb list-keys --name $COSMOSDB_ACCOUNT_NAME --resource-group $RESOURCE_GROUP --output tsv |awk '{print $1}')
MY_STORAGE_CONNECTION="DefaultEndpointsProtocol=https;AccountName=$STORAGE_ACCOUNT_NAME;AccountKey=$STORAGE_ACCOUNT_KEY;EndpointSuffix=core.windows.net"
MY_COSMOS_DB_CONNECTION="AccountEndpoint=https://$COSMOSDB_ACCOUNT_NAME.documents.azure.com:443/;AccountKey=$COSMOSDB_ACCOUNT_KEY;"
MY_COMPUTER_VISION_ENDPOINT=$(az cognitiveservices account show -n $COGNITIVE_ACCOUNT_NAME -g $COGNITIVE_RESOURCE_GROUP --output tsv |awk '{print $1}')
MY_COMPUTER_VISION_APIKEY=$(az cognitiveservices account keys list -n $COGNITIVE_ACCOUNT_NAME -g $COGNITIVE_RESOURCE_GROUP --output tsv |awk '{print $1}')

az webapp config appsettings set \
  -n $APP_NAME \
  -g $RESOURCE_GROUP \
  --settings \
  ComputerVisionSubscription=$MY_COMPUTER_VISION_APIKEY \
  ComputerVisionApiEndpoint=$MY_COMPUTER_VISION_ENDPOINT \
  MyStorageConnectionString=$MY_STORAGE_CONNECTION \
  MyCosmosDBConnectionString=$MY_COSMOS_DB_CONNECTION \

echo "Done"
