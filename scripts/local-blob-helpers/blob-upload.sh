#!/bin/sh

STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"

CONTAINER="upload"

if [ $# -ne 1 ]
then
    echo "$0 <filepath>"
    exit 1
fi

# Upload Vide file
LOCAL_FILE=$1
FILE_NAME=$(basename $LOCAL_FILE)
CONTAINER="upload-images"

az storage blob upload --container-name $CONTAINER --name $FILE_NAME --file $LOCAL_FILE --connection-string $STORAGE_CONNECTION_STRING

# List blobs in the container
az storage blob list --container-name $CONTAINER --output table --connection-string $STORAGE_CONNECTION_STRING

