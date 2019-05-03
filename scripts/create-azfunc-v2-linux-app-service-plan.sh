#!/bin/sh
set -e -x
#
# Create the Azure Functions on Linux ( App Service Plan )
#

RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
REGION="<REGION NAME: eastus>"
STORAGE_ACCOUNT="<STORAGE ACCOUNT NAME>"
PLAN_NAME="<APP SERVICE PLAN NAME>"
APP_NAME="<FUNCTION APP NAME>" #  the name needs to be unique across all apps in Azure.
# [NOTE]
# Linux Consumption plan is only available in limited regions
# see https://github.com/Azure/Azure-Functions/wiki/Azure-Functions-on-Linux-Preview#prerequisites

echo "Create Resource Group: $RESOURCE_GROUP"
az group create --name $RESOURCE_GROUP --location $REGION

echo "Create App Service Plan"
az appservice plan create --name $PLAN_NAME \
  --resource-group $RESOURCE_GROUP \
  --sku B1 --is-linux

echo "Create an Azure Storage account: $STORAGE_ACCOUNT"
az storage account create --name $STORAGE_ACCOUNT \
  --location $REGION \
  --resource-group $RESOURCE_GROUP \
  --sku Standard_LRS

echo "Create a empty function app on Linux (App Service Plan): $APP_NAME"
az functionapp create \
  --resource-group $RESOURCE_GROUP \
  --name $APP_NAME \
  --storage-account $STORAGE_ACCOUNT \
  --plan $PLAN_NAME \
  --runtime python

#echo "Clearning up all resources"
# az group delete --name $RESOURCE_GROUP

echo "Done"
