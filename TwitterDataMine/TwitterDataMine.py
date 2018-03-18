import json
import re
import tweepy
import operator
import wx
from collections import Counter
from tweepy import OAuthHandler

from displayUserData import displayUserData
from printFromJson import printFromJson
from configureAPI import configureAPI
from collectTweets import collectTweets
from ConfigureStep import ConfigureStep


def main():
    
    #configuring Twitter API
    api = configureAPI()
    
    collectTweets(api,"elonmusk",5)
    
    
if __name__=="__main__":
    main()