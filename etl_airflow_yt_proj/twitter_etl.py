import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "BqB22a8WDO3yCCI3T2x1Nk5VB"
access_secret = "mSfcm4xwJHZYQvrDU0UuhFFQwJQoa9YpCyBRGTteRIeVoouxT0"
consumer_key = "1285897943313117184-mWx2GSuIHQ2XT7LaSK4sU3Y4j2urVL"
consumer_secret = "qYHUS4kT8QRLb2x6mHJ7pnKHTdmxHcK0N1Kf2t3c7zuMe"

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

print(tweets)


