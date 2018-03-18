import json
import re
import tweepy
import operator

from collections import Counter
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from importKeys import importKeys
from displayUserData import displayUserData
from printFromJson import printFromJson
from firstRun import firstRun

import sys

def main():
    # get keys
    path = "C:\\Users\\krzst\\keys.txt"
    firstRun(path)

    keys = []
    keys = importKeys(path)
    
    consumer_key = keys[0]
    consumer_secret = keys[1]
    access_token = keys[2]
    access_secret = keys[3]
        
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth) 
    
    #targeting user
    target = 'chris_stezala09'
    number = 5
    print("Getting data for " + target)
    # watching target timeline
    for twt in tweepy.Cursor(api.user_timeline, id=target).items(number):
       printFromJson(twt._json)
    return twt
    
    
if __name__=="__main__":
    main()