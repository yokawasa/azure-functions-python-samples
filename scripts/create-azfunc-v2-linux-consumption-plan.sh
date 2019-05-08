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

RESOURCE_GROUP="RG-azfuncv2-t"
REGION="westus"
STORAGE_ACCOUNT="azfuncv2linuxstore2"
APP_NAME="yoichikaazfuncv2linux002" #  the name needs to be unique across all apps in Azure.

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
