import json
import hashlib
import datetime
import logging
import feedparser

import azure.functions as func

RSS_FEED_URL = "https://kubernetes.io/feed.xml"

def get_feed():
    feed=feedparser.parse(RSS_FEED_URL)
    retdocs=[]
    # Get 5 latest feeds
    latestentries=feed['entries'][:5]
    for entry in latestentries:
        idhash = hashlib.sha1( entry[ 'link' ].encode('utf-8')).hexdigest()
        retdoc= {
            "id": idhash,
            "title": entry[ 'title' ],
            "date": entry[ 'updated' ]
        }
        retdocs.append(retdoc)
    return retdocs

def main(mytimer: func.TimerRequest, outdoc: func.Out[func.Document]):
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')
    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    try:
        # Get Blog feeds
        outdata = {}
        outdata['items'] = get_feed()
        # logging.info(outdata)  # for debug

        # Store output data using Cosmos DB output binding
        outdoc.set(func.Document.from_json(json.dumps(outdata)))
    except Exception as e:
        logging.error('Error:')
        logging.error(e)