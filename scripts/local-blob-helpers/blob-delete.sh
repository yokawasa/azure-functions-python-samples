#!/bin/sh

STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"

CONTAINER="upload-images"

if [ $# -ne 1 ]
then
    echo "$0 <blobname>"
    exit 1
fi

# DELETE Blob
BLOB_NAME=$1
az storage blob delete -c $CONTAINER -n $BLOB_NAME --connection-string $STORAGE_CONNECTION_STRING
