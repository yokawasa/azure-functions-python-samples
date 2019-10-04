# http-trigger-blob-sas-token (Python)

- [http-trigger-blob-sas-token (Python)](#http-trigger-blob-sas-token-python)
  - [Local development](#local-development)
  - [Test access](#test-access)
  - [Publish the function to the cloud](#publish-the-function-to-the-cloud)

| Sample | Description | Trigger | In Bindings | Out Bindings
| ------------- | ------------- | ------------- | ----------- | ----------- |
| [http-trigger-dump-request](v2functions/http-trigger-dump-request) | Azure Function HTTP Trigger Python Sample that returns request dump info with JSON format | HTTP | NONE | HTTP |


## Local development
```sh
func host start
```

## Test access
```sh
curl -s http://localhost:7071/api/http-trigger-dump-request |jq
{
  "method": "GET",
  "url": "http://localhost:7071/api/http-trigger-dump-request",
  "headers": {
    "accept": "*/*",
    "host": "localhost:8080",
    "user-agent": "curl/7.54.0"
  },
  "params": {},
  "get_body": ""
}
```

## Publish the function to the cloud

Publish the function to the cloud
```sh
FUNCTION_APP_NAME="MyFunctionApp"
func azure functionapp publish $FUNCTION_APP_NAME
```
