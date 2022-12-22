from settings import *
import tweepy
import json
import datetime

#日本のトレンド上位50を取得してjsonで保存
def get_place_trends(woeid=23424856, data_dir='data'):
    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    #日本のWOEID
    # woeid=23424856
    #トレンド一覧取得
    trends = api.get_place_trends(woeid)

    time_now = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')

    with open(data_dir+'/trend/{}.json'.format(time_now), 'w') as f:
        json.dump(trends[0], f, indent=4, ensure_ascii=False)
