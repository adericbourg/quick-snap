#!/bin/env python

# Install python-twitter

import os
import sys
import twitter

twitter_consumer_key = os.environ['TWITTER_CONSUMER_KEY']
twitter_consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
twitter_access_token = os.environ['TWITTER_ACCESS_TOKEN']
twitter_access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

if len(sys.argv) < 2:
    print "No image provided"
    sys.exit(1)

api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token,
                  access_token_secret=twitter_access_token_secret)

image_path = sys.argv[1]
file = open(image_path, 'rb')
api.PostUpdate("", file)
