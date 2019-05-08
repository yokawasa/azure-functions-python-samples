#!/bin/sh
set -e -x
# Create Azure Resource group

RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
REGION="<REGION NAME: eastus>"

RESOURCE_GROUP="RG-azfuncv2-ta"
REGION="japanwest"

echo "Create Resource Group: $RESOURCE_GROUP"
az group create --name $RESOURCE_GROUP --location $REGION

echo "Done"
