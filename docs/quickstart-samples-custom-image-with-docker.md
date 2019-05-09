# Quickstart Function Samples as a Custom image with Docker

This is a quickstart on how you start running Python function samples as a custom image (Container) with Docker.

<!-- TOC -->
- [Quickstart Function Samples as a Custom image with Docker](#quickstart-function-samples-as-a-custom-image-with-docker)
  - [Prerequisites](#prerequisites)
  - [Git clone source code](#git-clone-source-code)
  - [Create Azure Resources that required to run the samples](#create-azure-resources-that-required-to-run-the-samples)
    - [[Required] Azure Storage Account](#required-azure-storage-account)
    - [[Optional] CosmosDB and Computer Vision API](#optional-cosmosdb-and-computer-vision-api)
  - [Build Container Image](#build-container-image)
  - [Run the image locally](#run-the-image-locally)
    - [1. Run the image with minimum configuration](#1-run-the-image-with-minimum-configuration)
    - [2. Run the image with full configuration](#2-run-the-image-with-full-configuration)
  - [Test access to the functions](#test-access-to-the-functions)
  - [Tips](#tips)
    - [Console Logging Option](#console-logging-option)
  - [LINKS](#links)


## Prerequisites
- [Docker](https://docs.docker.com/)

## Git clone source code
```bash
git clone https://github.com/yokawasa/azure-functions-python-samples.git
```

## Create Azure Resources that required to run the samples

This project include a set of multiple sample function and each function may have different required resources. Please check `readme.md` included in each function sample (Check [v2functions](../v2functions)). 

### [Required] Azure Storage Account
A minimum is an `Azure Storage Account` which is necessary for all functions. Here is how you create:

> [scripts/create-resource-group.sh](../scripts/create-resource-group.sh)
```bash
RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
REGION="<REGION NAME: eastus>"
az group create --name $RESOURCE_GROUP --location $REGION
```
> [scripts/create-storage-account.sh](../scripts/create-storage-account.sh)
```bash
RESOURCE_GROUP="<RESOURCE GROUPP MAME>"
REGION="<REGION NAME: eastus>"
STORAGE_ACCOUNT="<STORAGE ACCOUNT NAME>"

echo "Create an Azure Storage account: $STORAGE_ACCOUNT"
az storage account create --name $STORAGE_ACCOUNT \
  --location $REGION \
  --resource-group $RESOURCE_GROUP \
  --sku Standard_LRS
```

### [Optional] CosmosDB and Computer Vision API
The rest of resources such as Cosmos DB account and Computer Vision Subscription are optionals: 

For CosmosDB Account and its database and collections, you can leverage the following helper script. Adding required params in the script and running will create a CosmosDB Account and database and collections.
> [scripts/create-cosmosdb-test-db-coll.sh](../scripts/create-cosmosdb-test-db-coll.sh)

For Computer Vision API subscription, you can leverage the following helper script. Likewise, add required params in the script and run it.
> [scripts/create-cognitive-computer-vision.sh](../scripts/create-cognitive-computer-vision.sh)

## Build Container Image

Let's build the image from the Docker file using `docker build` command.

```bash
cd v2functions

# Build the image with `docker build` command
# docker build --tag <docker-id>/<imagename>:<tag> .
docker build --tag yoichikawasaki/azfuncpythonsamples:v0.0.1 .
```
You can also use a helper script - [scripts/docker-build.sh](../scripts/docker-build.sh)

##  Run the image locally

Now you're ready to run the app. You have 2 options

### 1. Run the image with minimum configuration

> [scripts/docker-run-mini.sh](../scripts/docker-run-mini.sh)
```bash
...
docker run -p 8080:80 -it \
  -e AzureWebJobsStorage="$STORAGE_CONNECTION_STRING" \
  $DOCKER_ID/$CONTAINER_IMAGE_NAME:$TAG
...
```

### 2. Run the image with full configuration

> [scripts/docker-run.sh](../scripts/docker-run.sh)
```bash
...
docker run -p 8080:80 -it \
  -e AzureWebJobsStorage="$STORAGE_CONNECTION_STRING" \
  -e MyStorageConnectionString="$STORAGE_CONNECTION_STRING" \
  -e MyCosmosDBConnectionString="$COSMOSDB_CONNECTION_STRING" \
  -e ComputerVisionSubscription="$COMPUTER_VSION_API_SUBSCRIPTION" \
  -e ComputerVisionApiEndpoint="$COMPUTER_VSION_API_ENDPOINT" \
  $DOCKER_ID/$CONTAINER_IMAGE_NAME:$TAG
...
```

## Test access to the functions

Once you start the app with docker, let's send a test request to `http-trigger-dump-request` function:

```bash
curl -s http://localhost:8080/api/http-trigger-dump-request |jq

{
  "method": "GET",
  "url": "http://localhost:8080/api/http-trigger-dump-request",
  "headers": {
    "accept": "*/*",
    "host": "localhost:8080",
    "user-agent": "curl/7.54.0"
  },
  "params": {},
  "get_body": ""
}
```

## Tips
### Console Logging Option
By default, Console Logging is not enabled, and you can enable it by setting the following option as an ENV variable in Dockerfile or giving the option in running docker:
```
ENV AzureFunctionsJobHost__Logging__Console__IsEnabled=true
```

## LINKS
- [Create a function on Linux using a custom image](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image)