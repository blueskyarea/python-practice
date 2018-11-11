#!/usr/bin/env python
# coding: utf-8

from requests_oauthlib import OAuth1Session
import json
import secret
import sys

args = sys.argv

# URL for keyword search
url = 'https://api.twitter.com/1.1/search/tweets.json'

if len(args) > 2:
  keyword = ''
  fileName = ''
  for arg in args:
    keyword = keyword + " " + arg
    fileName = fileName + "_" + fileName

keyword = keyword.strip()
fileName = fileName.strip()

f = open('latest_id_str_' + fileName)
latest_id_str = f.read()
f.close()
if latest_id_str == '':
  latest_id_str = 0

#keyword = 'Python'
params = {'q': keyword, 'since_id': int(latest_id_str),  'count': 100}

# GET by OAuth
twitter = OAuth1Session(secret.CK, secret.CS, secret.AT, secret.AS)
req = twitter.get(url, params = params)

tmp_latest_id_str = 0
f = open(fileName + '.txt', a)
if req.status_code == 200:
    timeline = json.loads(req.text)
    index = 1
    for each in timeline['statuses']:
        if keyword in each['text'] and 'RT' not in each['text']:
            user = each['user']
            f.write(index + '|' + each['id_str'] + '|' + user['name'] + '|' + user['location'] + '|' + each['text'] + '\n')
            if index == 1:
              tmp_latest_id_str = each['id_str']
            index+=1
else:
    print ("Error: %d" % req.status_code)
f.close()

f = open('latest_id_str_' + fileName, w+)
f.write(tmp_latest_id_str)
f.close()

