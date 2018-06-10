#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json


# タイムライン取得用のURL
#url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
url = 'https://api.twitter.com/1.1/search/tweets.json'

# とくにパラメータは無い
params = {'q': 'マクド', 'count': 10}

# OAuth で GET
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.get(url, params = params)

if req.status_code == 200:
    # レスポンスはJSON形式なので parse する
    timeline = json.loads(req.text)
    # 各ツイートの本文を表示
    #metadata = timeline['metadata']
    statuses = timeline['statuses']
    #print(statuses)
    st = json.dumps(statuses)
    dics = json.loads(st)
    for dic in dics:
        print('-----')
        print(dic['text'])
else:
    # エラーの場合
    print ("Error: %d" % req.status_code)
