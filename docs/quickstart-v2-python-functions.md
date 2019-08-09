# Quickstart V2 Python Functions with Azure Functions Core Tools

This is a quickstart on how you create and deploy a Python function on Azure Functions 2.X using the [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python).


<!-- TOC -->
- [Quickstart V2 Python Functions with Azure Functions Core Tools](#quickstart-v2-python-functions-with-azure-functions-core-tools)
  - [Prerequisites](#prerequisites)
  - [Create a Python functions project](#create-a-python-functions-project)
    - [Create Python functions from templates](#create-python-functions-from-templates)
    - [Create and activate a virtual environment](#create-and-activate-a-virtual-environment)
  - [Manage package with requirements.txt](#manage-package-with-requirementstxt)
    - [function.json](#functionjson)
  - [Update the host.json file to use extension bundles,](#update-the-hostjson-file-to-use-extension-bundles)
  - [Run the function locally](#run-the-function-locally)
  - [Publishing to Azure](#publishing-to-azure)
  - [LINKS](#links)


## Prerequisites
- Install `Python 3.6`
- Install [Azure Core Tools version 2.x](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2) (the latest one)

```bash
# Install the latest Azure Core Tools version 2.x
npm install -g azure-functions-core-tools
  
# If it's on macOS, you can install with homebrew
brew tap azure/functions
brew install azure-functions-core-tools
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

When you develop locally using the Azure Functions Core Tools or VS Code, I guess you simply install your required python packages uinsg `pip`. It's OK in developing locally but when it comes to the production deployment, Please make sure that all your dependencies are listed in the `requirements.txt`, located at the root of your project directory. For example, here is a requirements.txt where I added my required packages and its version for my sample function (For minimum packages, please refer to [this](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#python-version-and-package-management))

```txt
# Minimum packages for azure functions
azure-functions
azure-functions-worker
grpcio==1.14.1
grpcio-tools==1.14.1
protobuf==3.6.1
six==1.11.0

# Additional packages
numpy==1.15.4   
```

Here is how you install packages listed in `requirements.txt`
```sh
pip install -r requirements.txt
```

### function.json
Configure trigger, input and output binding with `function.json`. Please see [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python) for the detail


## Update the host.json file to use extension bundles, 

In version 2.x of the Azure Functions runtime, you have to explicitly register the binding extensions that you use in your function app. To use extension bundles, update the `host.json` file to include the following entry for extensionBundle:
> host.json
```json
{
    "version":  "2.0",
    "extensionBundle": {
        "id": "Microsoft.Azure.Functions.ExtensionBundle",
        "version": "[1.*, 2.0.0)"
    }
}
```
> [NOTE] As an alternative way, you can manually install extension bundles by running a command - `func extensions install` so appropritate binding extensions are installed in `bin` directory. But if you already added the entry for extensionBundle in `host.json` like above, you don't need this.
> ```bash
> # change directory to a project directory
> cd functions
> # Manually install extension bundles using func command (Azure Core Tools)
> func extensions install
> ```

## Run the function locally

From inside the project directory (e.g. `v2functions`), run:

```sh
func host start
```
For more detail, please refer to [Local development Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-register#local-development-azure-functions-core-tools)
> 

## Publishing to Azure

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
