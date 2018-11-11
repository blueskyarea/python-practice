#!/usr/bin/env python
# coding: utf-8

from requests_oauthlib import OAuth1Session
import json
import secret
import sys
import os
import emoji

args = sys.argv

# URL for keyword search
url = 'https://api.twitter.com/1.1/search/tweets.json'

if len(args) > 2:
  keyword = ''
  fileName = ''
  del args[0:1]
  for arg in args:
    keyword = keyword + " OR " + arg
    fileName = fileName + "_" + arg
  keyword = keyword[4:]
  fileName = fileName[1:]
else:
  keyword = args[1]
  fileName = args[1]

if os.path.exists('latest_id_str_' + fileName):
  f = open('latest_id_str_' + fileName)
  latest_id_str = f.read()
  if latest_id_str == '':
    latest_id_str = 1
  f.close()
else:
  latest_id_str = 1

#keyword = 'Python'
params = {'q': keyword, 'since_id': int(latest_id_str),  'count': 100}

# GET by OAuth
twitter = OAuth1Session(secret.CK, secret.CS, secret.AT, secret.AS)
req = twitter.get(url, params = params)

# function
def remove_emoji(src_str):
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)

tmp_latest_id = int(latest_id_str)
f = open(fileName + '.txt', 'a')
if req.status_code == 200:
    timeline = json.loads(req.text)
    index = 1
    for each in timeline['statuses']:
        print(keyword)
        if 'RT' not in each['text']:
            user = each['user']
            f.write(str(index) + '|' + each['id_str'] + '|' + each['created_at'] + '|' + user['name'] + '|' + user['location'] + '|' + remove_emoji(each['text'].replace('\n', ' ')) + '\n')
            if index == 1:
              tmp_latest_id = each['id_str']
            index+=1
else:
    print ("Error: %d" % req.status_code)
f.close()

f = open('latest_id_str_' + fileName, 'w+')
f.write(str(tmp_latest_id))
f.close()

