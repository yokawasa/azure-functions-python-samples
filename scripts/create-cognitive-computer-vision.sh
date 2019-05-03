#!/bin/sh
#
# Create Cognitive Computer Vision Resource
#

COGNITIVE_RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
REGION="<REGION NAME: eastus>"
COGNITIVE_ACCOUNT_NAME="<COGNITIVE ACCOUNT NAME>"

## KIND
# You can get list of kinds with the following command:
# az cognitiveservices account list-kinds
# [
#  "AnomalyDetector",
#  "Bing.Autosuggest.v7",
#  "Bing.CustomSearch",
#  "Bing.EntitySearch",
#  "Bing.Search.v7",
#  "Bing.SpellCheck.v7",
#  "CognitiveServices",
#  "ComputerVision",
#  "ContentModerator",
#  "CustomVision.Prediction",
#  "CustomVision.Training",
#  "Dummy",
#  "Face",
#  "InkRecognizer",
#  "Internal.AllInOne",
#  "LUIS",
#  "Personalizer",
#  "QnAMaker",
#  "SpeakerRecognition",
#  "SpeechServices",
#  "TextAnalytics",
#  "TextTranslation"
# ]

echo "Create Resource Group: $COGNITIVE_RESOURCE_GROUP"
az group create --name $COGNITIVE_RESOURCE_GROUP --location $REGION

echo "Create Cognitive Resource for Computer Vision: $COGNITIVE_ACCOUNT_NAME"
az cognitiveservices account create \
  -n $COGNITIVE_ACCOUNT_NAME \
  -g $COGNITIVE_RESOURCE_GROUP \
  --kind ComputerVision \
  --sku S1 \
  -l $REGION \
  --yes

## NOTE
## `--yes`:  Do not prompt for terms confirmation.

API_ENDPOINT=$(az cognitiveservices account show -n $COGNITIVE_ACCOUNT_NAME -g $COGNITIVE_RESOURCE_GROUP --output tsv |awk '{print $1}')
API_KEY=$(az cognitiveservices account keys list -n $COGNITIVE_ACCOUNT_NAME -g $COGNITIVE_RESOURCE_GROUP --output tsv |awk '{print $1}')

echo "API Endpoint: ${API_ENDPOINT}"
echo "API KEY: ${API_KEY}"

echo "Done"
