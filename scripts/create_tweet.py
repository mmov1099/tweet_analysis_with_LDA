import tweepy
from settings import *

def tweet(query:str):
    client = tweepy.Client(
        consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET
    )

    # Create Tweet

    # The app and the corresponding credentials must have the Write permission

    # Check the App permissions section of the Settings tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps

    # Make sure to reauthorize your app / regenerate your access token and secret 
    # after setting the Write permission

    response = client.create_tweet(
        text=query
    )
    print(f"https://twitter.com/user/status/{response.data['id']}")