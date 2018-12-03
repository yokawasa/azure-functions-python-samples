#!/bin/sh

set -e -x

echo "Installing the Azure CLI extension for the Azure Functions Linux Consumption preview..."

curl "https://functionscdn.azureedge.net/public/docs/functionapp-0.0.1-py2.py3-none-any.whl" -o functionapp-0.0.1-py2.py3-none-any.whl
az extension add --source functionapp-0.0.1-py2.py3-none-any.whl
