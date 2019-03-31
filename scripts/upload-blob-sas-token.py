import sys
import os
import ntpath
import json 
import requests

_AZFUNC_API_KEY="AZURE_FUNCTION_KEY: ex. aRVQ7Lj0vzDhY0JBYF8gpxYyEBxLwhO51JSC7X5dZFbTvROs7xNg=="
_AZFUNC_API_URL="AZURE_FUNCTION_ENDPOINT: ex. https://<app_account>.azurewebsites.net/api/<func_name>"

if __name__ == '__main__':
    
    file_path = "/tmp/test.jpg"
    content_type = "image/jpeg"
    container_name = "functiontest"

    file_name = ntpath.basename(file_path)

    ### Getting SAS token for uploading files to Azure Blob Storage
    payload = {
        "permission": "awl",
        "container": container_name,
        "blobname": file_name
    }
    r = requests.post(_AZFUNC_API_URL,
            headers = {
                "Content-Type" : "application/json; charset=UTF-8",
                "x-functions-key": _AZFUNC_API_KEY
            },
            data=json.dumps(payload)
        )
    if r.status_code != 200:
        print(f"Getting SAS token request result: status code={r.status_code}")
        sys.exit(1) 

    content_dict = json.loads(r.content.decode())
    url = content_dict['url'] 

    ### Uploading files to Azure Blob Storage
    with open(file_path , 'rb') as filehandle:
        r = requests.put(url,
                data=filehandle,
                headers={
                    'Content-Type': content_type,
                    'x-ms-blob-type': 'BlockBlob'
                },
                params={
                    'file': file_path
                }
            )
        print(f"Uploading request result: status code={r.status_code}")
