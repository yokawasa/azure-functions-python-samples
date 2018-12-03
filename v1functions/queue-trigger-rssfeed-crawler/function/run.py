# -*- coding: utf-8 -*-

"""

Azure Functions Queue Trigger Python Sample
- Get RSS feed URL from Queue and dump all items that obtained from RSS feed

"""

import os
import sys
sys.path.append("site-packages")
import feedparser

# Read the queue message
rss_feed_url = open(os.environ['inputMessage']).read()
print "Python script processes rss feed: '{0}'".format(rss_feed_url)

# Get RSS feed by using feedparser module
feed=feedparser.parse(rss_feed_url)

# Dump RSS feed obtained
print feed.feed.title.encode('utf-8')
for entry in feed[ 'entries' ]:
    print "Title: ", entry[ 'title' ].encode('utf-8')
    print "URL: ", entry[ 'link' ]
    print "Description: ", entry[ 'description' ].encode('utf-8')
    print "Date: ", entry[ 'updated' ]
