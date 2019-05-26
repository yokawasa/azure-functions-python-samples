#!/bin/sh
set -e -x

cwd=`dirname "$0"`
expr "$0" : "/.*" > /dev/null || cwd=`(cd "$cwd" && pwd)`

#############################################################
#  params
#############################################################
DOCKER_ID="<Docker ID>"
CONTAINER_IMAGE_NAME="<Container Image Name>"
RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
REGION="<REGION NAME: eastus>"
STORAGE_ACCOUNT_NAME="<STORAGE ACCOUNT NAME>"
COSMOSDB_ACCOUNT_NAME="<COSMOSDB ACCOUNT NAME>"
COGNITIVE_ACCOUNT_NAME="<COGNITIVE ACCOUNT NAME>"
COGNITIVE_RESOURCE_GROUP="<COGNITIVE RESOURCE GROUP>"
#############################################################

FUNC_PROJECT_DIR="$cwd/../v2functions"

TAG=`cat $FUNC_PROJECT_DIR/VERSION`

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


docker run -p 8080:80 -it \
  -e AzureWebJobsStorage="$STORAGE_CONNECTION_STRING" \
  -e MyStorageConnectionString="$STORAGE_CONNECTION_STRING" \
  -e MyCosmosDBConnectionString="$COSMOSDB_CONNECTION_STRING" \
  -e ComputerVisionSubscription="$COMPUTER_VSION_API_SUBSCRIPTION" \
  -e ComputerVisionApiEndpoint="$COMPUTER_VSION_API_ENDPOINT" \
  -e AzureFunctionsJobHost__Logging__Console__IsEnabled="true" \
  $DOCKER_ID/$CONTAINER_IMAGE_NAME:$TAG
