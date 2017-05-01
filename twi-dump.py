import json
import re
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
from ntk import nounPhrase

# import twitter keys and tokens
from config import *

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '591599507-NCY2bzBKVPGpZ1eBn9b9g3tpR8K1CHOFhsSGgNi4'
ACCESS_SECRET = 'v1YWJrH0JbvLCTseNwegK0q8FHcuf0k6iQKNP5ZweOTpf'
CONSUMER_KEY = 'eFvjfaNKBIm4N8OOWklzvo0Wz'
CONSUMER_SECRET = 'gqHMsiDuiCd8Bl0hsRgD6mkEtpnExixuyveOBPJm3JVplyoGW9'

# create instance of elasticsearch
es = Elasticsearch()
i=0



class TweetStreamListener(StreamListener):

    # on success
    def on_data(self, data):

        # decode json
        dict_data = json.loads(data)

        # pass tweet into TextBlob
        try:
            tweet = TextBlob(dict_data["text"])
            polarity = tweet.sentiment.polarity
            subjectivity = tweet.sentiment.subjectivity
            text = dict_data["text"]
        except KeyError:
            print ('error')
            return True

        # output sentiment polarity
        print polarity
        
        text = re.sub('[[h|H]ttp|https]','',text)
        text = re.sub('rt','',text)
        text = re.sub('co','',text)
        nonP = nounPhrase(text)

        # determine if sentiment is positive, negative, or neutral
        if polarity < 0:
            sentiment = "negative"
        elif polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output sentiments
        print sentiment

        # add text and sentiment info to elasticsearch
        es.index(index="sentiment",
                 doc_type="test-type",
                 body={"username": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "tweet": text,
                       "nounPhrase": nonP,
                       "polarity": polarity,
                       "subjectivity": subjectivity,
                       "sentiment": sentiment})
        return True

    # on failure
    def on_error(self, status):
        print status

if __name__ == '__main__':

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # create instance of the tweepy stream
    stream = Stream(auth, listener)

    # search twitter for "congress" keyword
    #stream.filter(track=['Trump','trump','#trump','usa','#usa','USA','#USA'],languages=["en"])
    stream.sample(languages=["en"])
