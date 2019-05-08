FROM mcr.microsoft.com/azure-functions/python:2.0

COPY . /home/site/wwwroot

ENV AzureFunctionsJobHost__Logging__Console__IsEnabled=true

RUN cd /home/site/wwwroot && \
    pip install -r requirements.txt
