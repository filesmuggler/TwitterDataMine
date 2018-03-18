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


def main():
    
    #configuring Twitter API
    api = configureAPI()
    
    
    
    
if __name__=="__main__":
    main()