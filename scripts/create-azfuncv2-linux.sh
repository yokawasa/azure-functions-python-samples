#!/bin/sh
set -e -x
#
# refs
# https://docs.microsoft.com/en-us/cli/azure/functionapp?view=azure-cli-latest
#

RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
REGION="<REGION NAME: eastus>"
STORAGE_ACCOUNT="<STORAGE ACCOUNT NAME>"
APP_SERVICE_PLAN="<APP SERVICE PLAN NAME>"
APP_NAME="<FUNCTION APP NAME>" #  the name needs to be unique across all apps in Azure.
DEPLOY_SOURCE_URL="https://github.com/Azure-Samples/functions-quickstart-linux"

echo "Create Resource Group: $RESOURCE_GROUP"
az group create --name $RESOURCE_GROUP --location $REGION

echo "Create an Azure Storage account: $STORAGE_ACCOUNT"
az storage account create --name $STORAGE_ACCOUNT \
    --location $REGION \
    --resource-group $RESOURCE_GROUP \
    --sku Standard_LRS

echo "Create a Linux App Service plan: $APP_SERVICE_PLAN"
az appservice plan create --name $APP_SERVICE_PLAN \
    --resource-group $RESOURCE_GROUP \
    --sku B1 \
    --is-linux

echo "Create a empty function app on Linux: $APP_NAME"
az functionapp create --name $APP_NAME \
    --storage-account $STORAGE_ACCOUNT \
    --resource-group $RESOURCE_GROUP \
    --plan $APP_SERVICE_PLAN 

#echo "Create a function app on Linux based on deployment source: $APP_NAME"
#az functionapp create --name $APP_NAME \
#    --storage-account $STORAGE_ACCOUNT \
#    --resource-group $RESOURCE_GROUP \
#    --plan $APP_SERVICE_PLAN \
#    --deployment-source-url https://github.com/Azure-Samples/functions-quickstart-linux

#echo "Clearning up all resources"
# az group delete --name $RESOURCE_GROUP

echo "Done"
