import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


def run_twitter_etl():

    access_key = ""
    access_secret = ""
    consumer_key = ""
    consumer_secret = ""

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)


    # Creating an API object
    api = tweepy.API(auth=auth)

    tweets = api.user_timeline(screen_name= '@elonmusk',
                            # 200 is the max tweets
                            count=200,
                            include_rts = False,
                            # Necessary to keep full_text
                            # Otherwise only the first 140 words are working
                            tweet_mode = "extended"
                            )


    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {
            "user": tweet.user.screen_name,
            "text": text,
            "like_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": tweet.created_at
        }

        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv("s3://airflow-proj/elonmusk_tweets.csv")