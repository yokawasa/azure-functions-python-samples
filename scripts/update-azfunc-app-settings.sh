#!/bin/sh
set -e -x

RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
APP_NAME="<FUNCTION APP NAME>" 
STORAGE_ACCOUNT_NAME="<STORAGE ACCOUNT NAME>"
COSMOSDB_ACCOUNT_NAME="<COSMOSDB ACCOUNT NAME>"
COGNITIVE_ACCOUNT_NAME="<COGNITIVE ACCOUNT NAME>"
COGNITIVE_RESOURCE_GROUP="<COGNITIVE RESOURCE GROUP>"


STORAGE_CONNECTION_STRING=$(az storage account show-connection-string \
--resource-group $RESOURCE_GROUP --name $STORAGE_ACCOUNT_NAME \
--query connectionString --output tsv)

COSMOSDB_CONNECTION_STRING=$(az cosmosdb list-connection-strings \
--resource-group $RESOURCE_GROUP --name $COSMOSDB_ACCOUNT_NAME \
--query connectionStrings --output tsv | head -1 |  awk '{print $1}')

COMPUTER_VSION_API_ENDPOINT=$(az cognitiveservices account show \
-n $COGNITIVE_ACCOUNT_NAME -g $COGNITIVE_RESOURCE_GROUP --output tsv |awk '{print $1}')

COMPUTER_VSION_API_SUBSCRIPTION=$(az cognitiveservices account keys list \
-n $COGNITIVE_ACCOUNT_NAME -g $COGNITIVE_RESOURCE_GROUP --output tsv |awk '{print $1}')

az webapp config appsettings set \
  -n $APP_NAME \
  -g $RESOURCE_GROUP \
  --settings \
  ComputerVisionSubscription=$COMPUTER_VSION_API_SUBSCRIPTION \
  ComputerVisionApiEndpoint=$COMPUTER_VSION_API_ENDPOINT=\
  MyStorageConnectionString=$STORAGE_CONNECTION_STRING \
  MyCosmosDBConnectionString=$COSMOSDB_CONNECTION_STRING

echo "Done"
