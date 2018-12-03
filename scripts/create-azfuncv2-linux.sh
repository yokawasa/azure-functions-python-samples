#!/bin/sh
set -e -x
#
# refs
# https://docs.microsoft.com/en-us/cli/azure/functionapp?view=azure-cli-latest
#

RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
REGION="<REGION NAME: eastus>"
STORAGE_ACCOUNT="<STORAGE ACCOUNT NAME>"
APP_NAME="<FUNCTION APP NAME>" #  the name needs to be unique across all apps in Azure.

echo "Create Resource Group: $RESOURCE_GROUP"
az group create --name $RESOURCE_GROUP --location $REGION

echo "Create an Azure Storage account: $STORAGE_ACCOUNT"
az storage account create --name $STORAGE_ACCOUNT \
    --location $REGION \
    --resource-group $RESOURCE_GROUP \
    --sku Standard_LRS

echo "Create a empty function app on Linux (Preview): $APP_NAME"
az functionapp createpreviewapp --name $APP_NAME \
    --resource-group $RESOURCE_GROUP \
    --storage-account $STORAGE_ACCOUNT \
    -l $REGION \
    --runtime python \
    --is-linux

#echo "Clearning up all resources"
# az group delete --name $RESOURCE_GROUP

echo "Done"
