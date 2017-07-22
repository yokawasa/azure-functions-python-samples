# proxies-simple-condition-matches
Azure Functions Python Sample that re-write dynamic and static page url using Azure Functions Proxies

| Trigger | In/Out Bindings |
------------ | ----------- |
| HTTP Trigger | output:HTTP |


## Proxies Configuration
```
{
    "$schema": "http://json.schemastore.org/proxies",
    "proxies": {
        "url-rewrite-static": {
            "matchCondition": {
                "route": "/static/{page}",
                "methods": [
                    "GET"
                ]
            },
            "backendUri": "https://<your-blob-account>.blob.core.windows.net/staticpage/{page}"
        },
        "url-rewrite-dynamic": {
            "matchCondition": {
                "route": "/content/{contentid}"
            },
            "backendUri": "https://<func_app_account>.azurewebsites.net/api/<func_name>?contentid={contentid}"
        }
    }
}
```


## Sample Access

For static access
```
https://<func_app_account>.azurewebsites.net/static/lasvegas.html
```
![](https://github.com/yokawasa/azure-functions-python-samples/raw/master/proxies-simple-condition-matches/img/static-page-result.png)

For dynamic access
```
https://<func_app_account>.azurewebsites.net/content/{contentid}
```
![](https://github.com/yokawasa/azure-functions-python-samples/raw/master/proxies-simple-condition-matches/img/dynamic-page-result.png)


## LINKS
- [Work with Azure Functions Proxies](https://docs.microsoft.com/en-us/azure/azure-functions/functions-proxies)
