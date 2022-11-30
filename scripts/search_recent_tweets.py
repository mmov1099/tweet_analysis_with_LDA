import tweepy
from settings import *
import json
import datetime

#queryのワードで検索して上位max_results個のツイートをjsonで保存
def search_recent_tweets(query:str, max_results:int=100):
    bearer_token = BEARER_TOKEN
    client = tweepy.Client(bearer_token)

    # Search Recent Tweets

    # This endpoint/method returns Tweets from the last seven days
    # By default, this endpoint/method returns 10 results
    # You can retrieve up to 100 Tweets by specifying max_results

    response = client.search_recent_tweets(query, max_results=max_results)
    # The method returns a Response object, a named tuple with data, includes,
    # errors, and meta fields
    # print(response.meta)

    # In this case, the data field of the Response returned is a list of Tweet
    # objects
    tweets = response.data

    # Each Tweet object has default ID and text fields
    # for tweet in tweets:
    #     print(tweet.id)
    #     print(tweet.text)

    #保存
    tweets_list = []

    for tweet in tweets:
        temp_tweet = dict(tweet)
        tweets_list.append(temp_tweet)

    tweets_dict = {'tweets':tweets_list}

    time_now = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')

    with open('../data/tweet/{}_{}.json'.format(time_now, query), 'w') as f:
        json.dump(tweets_dict, f, indent=4, ensure_ascii=False)

def main():
    print('pass')

if __name__ == '__main__':
    main()