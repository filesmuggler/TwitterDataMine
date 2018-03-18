import json
import re
import tweepy
import operator

from collections import Counter
from tweepy import OAuthHandler
from displayUserData import displayUserData
from printFromJson import printFromJson
from configureAPI import configureAPI

def main():
    
    #configuring Twitter API
    api = configureAPI()

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