# [Deprecated] How to install Python modules (1.X Function runtime)

**IMPORTANT - Please consider to use 2.X Python funciton as Python function in Azure function 1.X is experimental and new feature investments won't be added to 1.X Python function**

Basically there are 2 ways for you to install python modules
* 1. Installing python module using pip 
* 2. Uploading python module files via Kudu UI/Console


## 1. Installing python module using pip 

Here is how you install python module using pip in Kudu DebugConsole. 

Assuming you want to install feedparser module,


1-1. Open Kudu Debug Console: https://APPNAME.scm.azurewebsites.net/DebugConsole

1-2. (Optional) Check current installed module list
```
D:\home> python -m pip list
```
You will see the following output
```
    pip (1.5.6)
    setuptools (6.0.2)
    virtualenv (1.11.6)
```
1-3. CD to your function's base directory
```
D:\home> cd site\wwwroot\<your-function-name>
```
1-4. Create virtual env on your function's directory and activate it
```
D:\home\site\wwwroot\<your-function-name> python -m virtualenv myenv
D:\home\site\wwwroot\<your-function-name> cd myenv\Scripts
D:\home\site\wwwroot\<your-function-name>\myenv\Scripts> activate.bat
(myenv) D:\home\site\wwwroot\<your-function-name>\myenv\Scripts>
```
1-5. (Optional) Update the pip module to latest one 
```
(myenv) D:\home\site\wwwroot\<your-function-name>\myenv\Scripts>python -m pip install -U pip
```
You will see the following output
```
    Downloading/unpacking pip from https://pypi.python.org/packages/b6/ac/7015eb97dc749283ffdec1c3a88ddb8ae03b8fad0f0e611408f196358da3/pip-9.0.1-py2.py3-none-any.whl#md5=297dbd16ef53bcef0447d245815f5144
    Installing collected packages: pip
        Found existing installation: pip 1.5.6
            Uninstalling pip:
            Successfully uninstalled pip
    Successfully installed pip
    Cleaning up...
```
1-6. Install the module you want. Here you install feedparser
```
(myenv) D:\home\site\wwwroot\<your-function-name>\myenv\Scripts>python -m pip install feedparser
```

Once you install the module, you can leverage it in your function code. Don't forget to include the package path for the module in the PATH like this: 

```
# -*- coding: utf-8 -*-
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'myenv/Lib/site-packages')))
import feedparser
```

That's it!

Please also refer to 'Azure App Service Kudu console' secion of the page: [Managing Python on Azure App Service](https://docs.microsoft.com/en-us/visualstudio/python/managing-python-on-azure-app-service)

## 2. Uploading python module files via Kudu UI/DebugConsole

This is very straightfoward approach - you simply download the module and upload it using Kudo Debug Console. Just upload files and folder using drag and drop onto your function's base directory. 
https://github.com/projectkudu/kudu/wiki/Kudu-console

Once you upload the module files, then include the package path for the module in the PATH like (1) above.

This seems very easy but you have to prepare the right packages that is compatible with your function's platform - this is the tougheast point in this procedure. 

