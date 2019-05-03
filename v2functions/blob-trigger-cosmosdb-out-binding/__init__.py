import logging
import os
import azure.functions as func
import http.client, urllib.parse, base64, json
import requests

subscription_key = os.environ['ComputerVisionSubscription']
api_endpoint = os.environ['ComputerVisionApiEndpoint']

headers = {
    # Request headers.
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Description',
    'language': 'en',
})

def main(myblob: func.InputStream, doc: func.Out[func.Document]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    img_data = myblob.read()
    try:
        api_url = "{0}vision/v1.0/analyze?{1}".format(api_endpoint, params)
        logging.info("API URL:{}".format(api_url))

        r = requests.post(api_url,
                    headers=headers,
                    data=img_data)

        parsed = r.json()
        logging.info("Response:")
        logging.info(json.dumps(parsed, sort_keys=True, indent=2))

        # Set output data
        outdata = {}
        outdata['name'] = myblob.name
        taglist = parsed['description']['tags']
        outdata['text'] =  ' '.join(taglist)
        logging.info(json.dumps(outdata, sort_keys=True, indent=2))

        ## Store output data using Cosmos DB output binding
        doc.set(func.Document.from_json(json.dumps(outdata)))
    except Exception as e:
        print('Error:')
        print(e)
