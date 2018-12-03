# -*- coding: utf-8 -*-

"""

Azure Functions Queue Trigger Python Sample
- Get RSS feed URL from Queue and store all items that obtained from RSS feed

"""

import os
import sys
import json
import hashlib
#sys.path.append("site-packages")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'myenv/Lib/site-packages')))
import feedparser

# Read the queue message
rss_feed_url = open(os.environ['inputMessage']).read()
#rss_feed_url = "https://azure.microsoft.com/en-us/blog/feed/"
print "Python script processes rss feed: '{0}'".format(rss_feed_url)

# Get RSS feed by using feedparser module
feed=feedparser.parse(rss_feed_url)

# Collect all RSS feed obtained and store them into Document DB
outdocs=[]
for entry in feed[ 'entries' ]:
    idhash = hashlib.sha1( entry[ 'link' ]).hexdigest()
    outdoc= {
        "id": idhash,
        "title": entry[ 'title' ].encode('utf-8'),
        "description": entry[ 'description' ].encode('utf-8'),
        "date": entry[ 'updated' ]
    }
    print(outdoc)
    outdocs.append(outdoc)

# Writing to DocumentDB (Document parameter name: outputDocument)
with open(os.environ['outputDocument'], 'wb') as f:
    json.dump(outdocs,f)
