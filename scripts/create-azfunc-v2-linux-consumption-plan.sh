#!/bin/sh
set -e -x
#
# Create the Azure Functions on Linux ( Consumption Plan )
# [NOTE] Linux Consumption Preview is in preview

RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
REGION="<REGION NAME: eastus>"
STORAGE_ACCOUNT="<STORAGE ACCOUNT NAME>"
APP_NAME="<FUNCTION APP NAME>" #  the name needs to be unique across all apps in Azure.
# [NOTE]
# Linux Consumption plan is only available in limited regions
# see https://github.com/Azure/Azure-Functions/wiki/Azure-Functions-on-Linux-Preview#prerequisites

echo "Create Resource Group: $RESOURCE_GROUP"
az group create --name $RESOURCE_GROUP --location $REGION

echo "Create an Azure Storage account: $STORAGE_ACCOUNT"
az storage account create --name $STORAGE_ACCOUNT \
  --location $REGION \
  --resource-group $RESOURCE_GROUP \
  --sku Standard_LRS

echo "Create a empty function app on Linux (Consumption Plan): $APP_NAME"
az functionapp create \
  --resource-group $RESOURCE_GROUP \
  --name $APP_NAME \
  --storage-account $STORAGE_ACCOUNT \
  --os-type Linux \
  --consumption-plan-location $REGION \
  --runtime python

#echo "Clearning up all resources"
# az group delete --name $RESOURCE_GROUP

echo "Done"
