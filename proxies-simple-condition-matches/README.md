# proxies-simple-condition-matches
Azure Functions Python Sample that re-write dynamic and static url using Azure Functions Proxies

| Trigger | In/Out Bindings |
------------ | ----------- |
| HTTP Trigger | output:HTTP |


## Sample Access

For static access
```
https://<app_account>.azurewebsites.net/static/lasvegas.html
```
![](https://github.com/yokawasa/azure-functions-python-samples/raw/master/proxies-simple-condition-matches/img/static-page-result.png)

For dynamic access
```
https://<app_account>.azurewebsites.net/content/{contentid}
```
![](https://github.com/yokawasa/azure-functions-python-samples/raw/master/proxies-simple-condition-matches/img/dynamic-page-result.png)


## LINKS
- [Work with Azure Functions Proxies](https://docs.microsoft.com/en-us/azure/azure-functions/functions-proxies)