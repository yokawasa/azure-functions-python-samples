import logging

import azure.functions as func
import http.client, urllib.parse, base64, json
import requests

subscription_key = '<Computer Vision API Subscription Key>'

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

#def main(myblob: func.InputStream):
def main(myblob: func.InputStream, doc: func.Out[func.Document]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    img_data = myblob.read()
    try:
        api_url = "https://westus.api.cognitive.microsoft.com/vision/v1.0/analyze?%s" % params
        print ("API URL:{}".format(api_url))
        r = requests.post(api_url,
                    headers=headers,
                    data=img_data)

        parsed = r.json()
        logging.info("Response:")
        logging.info(json.dumps(parsed, sort_keys=True, indent=2))

        # Set CosmosDB
        outdata = {}
        outdata['image'] = myblob.name
        outdata['tags'] = parsed['description']['tags']
        logging.info(json.dumps(outdata, sort_keys=True, indent=2))
        doc.set(func.Document.from_json(json.dumps(outdata)))
    except Exception as e:
        print('Error:')
        print(e)
