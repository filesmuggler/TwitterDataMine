import tweepy
import os

from tweepy import OAuthHandler
from firstRun import firstRun
from importKeys import importKeys

def configureAPI():
    # get keys
    path =  os.getcwd() + "\\config_file.txt"
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

    return api