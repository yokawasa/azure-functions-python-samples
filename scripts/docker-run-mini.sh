#!/bin/sh
set -e -x

cwd=`dirname "$0"`
expr "$0" : "/.*" > /dev/null || cwd=`(cd "$cwd" && pwd)`

#############################################################
#  params
#############################################################
DOCKER_ID="<Docker ID>"
CONTAINER_IMAGE_NAME="<Container Image Name>"
RESOURCE_GROUP="<RESOURCE GROUP>"
STORAGE_ACCOUNT_NAME="<STORAGE ACCOUNT NAME>"
#############################################################

FUNC_PROJECT_DIR="$cwd/../v2functions"

TAG=`cat $FUNC_PROJECT_DIR/VERSION`

STORAGE_CONNECTION_STRING=$(az storage account show-connection-string \
--resource-group $RESOURCE_GROUP --name $STORAGE_ACCOUNT_NAME \
--query connectionString --output tsv)

docker run -p 8080:80 -it \
  -e AzureWebJobsStorage="$STORAGE_CONNECTION_STRING" \
  -e AzureFunctionsJobHost__Logging__Console__IsEnabled="true" \
  $DOCKER_ID/$CONTAINER_IMAGE_NAME:$TAG
