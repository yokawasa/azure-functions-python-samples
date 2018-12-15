# Quickstart V2 Python Functions

## Prerequisites
- Install Python 3.6
- Install [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2) version 2.2.70 or later


```sh
# Linux & Windows
$ npm install -g azure-functions-core-tools

# Mac
$ brew tap azure/functions
$ brew install azure-functions-core-tools 
```

## Create a Python functions project
```sh
$ func init v2functions --worker-runtime python
```

### Create Python functions from templates
List all python functions
```sh
$ func templates list

Python Templates:
  Azure Blob Storage trigger
  Azure Cosmos DB trigger
  Azure Event Grid trigger
  Azure Event Hub trigger
  HTTP trigger
  Azure Queue Storage trigger
  Azure Service Bus Queue trigger
  Azure Service Bus Topic trigger
  Timer trigger
  ...
```

Then, create a python function from templates
```sh
# First of all, move to pythoh functions project top
$ cd v2functions

# Http Trigger functions
$ func new --language python --template "HttpTrigger" --name HttpTriggerPY

# Blob Trigger functions
$ func new --language python --template "Azure Blob Storage trigger" --name BlobTriggerPY  

# Cosmos DB Trigger functions
$ func new --language python --template "Azure Cosmos DB trigger" --name CosmosdbTriggerPY
```

### Create and activate a virtual environment

Create a virtual environment directory at the top of function directory
```sh
cd functions
python3.6 -m venv .env
source .env/bin/activate
```

After activate your virtual enviroment for the function development, install packages you use in your functions (For example, `numpy`)
```sh
pip install --upgrade pip
pip install numpy
...
```

## Manage package with requirements.txt

When you develop locally using the Azure Functions Core Tools or VS Code, I guess you simply install your required python packages uinsg `pip`. It's OK in developing locally but when it comes to the production deployment, Please make sure that all your dependencies are listed in the `requirements.txt`, located at the root of your project directory. For example, here is a requirements.txt where I added my required packages and its version for my sample function 

```txt
azure-functions==1.0.0a5
azure-functions-worker==1.0.0a6
gensim==3.6.0
numpy==1.15.4
```

Here is how you install packages listed in `requirements.txt`
```sh
pip install -r requirements.txt
```

### function.json
Configure trigger, input and output binding with `function.json`. Please see [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python) for the detail

## Run the function locally
```sh
$ func host start
```

### Publishing to Azure

```sh
APP_NAME="your function name"
func azure functionapp publish $APP_NAME
```

If you got ERROR like this, do publish with `--build-native-deps` option
```
There was an error restoring dependencies.ERROR: cannot install vsts-cd-manager-1.0.2 dependency: binary dependencies without wheels are not supported.  Use the --build-native-deps option to try building the binary dependenciesusing a Docker container.
```
Publishing  with `--build-native-deps` option:
```sh
func azure functionapp publish $APP_NAME --build-native-deps
```

If you're unable to import your modules, try publishing again using the `--no-bundler` option ( See also [this doc](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python) for more detail):
```sh
func azure functionapp publish $APP_NAME --build-native-deps --no-bundler
```


## LINKS
- [Work with Azure Functions Core Tools V2](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2)
- [Create your first Python function in Azure](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python)
- [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
