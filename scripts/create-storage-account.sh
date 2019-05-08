#!/bin/sh
set -e -x
# Create Azure Storage Account 

RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
REGION="<REGION NAME: eastus>"
STORAGE_ACCOUNT="<STORAGE ACCOUNT NAME>"

RESOURCE_GROUP="RG-azfuncv2-ta"
REGION="japanwest"
STORAGE_ACCOUNT="azfuncv2linuxstore3"

echo "Create an Azure Storage account: $STORAGE_ACCOUNT"
az storage account create --name $STORAGE_ACCOUNT \
  --location $REGION \
  --resource-group $RESOURCE_GROUP \
  --sku Standard_LRS

echo "Done"
