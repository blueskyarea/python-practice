#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import secret

# URL for keyword search
url = 'https://api.twitter.com/1.1/search/tweets.json'

keyword = 'Python'
params = {'q': keyword, 'count': 10}

# GET by OAuth
twitter = OAuth1Session(secret.CK, secret.CS, secret.AT, secret.AS)
req = twitter.get(url, params = params)

if req.status_code == 200:
    timeline = json.loads(req.text)
    statuses = timeline['statuses']
    for each in timeline['statuses']:
        print('-----')
        print(each['text'])
else:
    print ("Error: %d" % req.status_code)
