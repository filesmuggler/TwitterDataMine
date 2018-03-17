import tweepy
import json
import re

from tweepy import OAuthHandler
from importKeys import importKeys

def main():
    # get keys
    path = "C:\\Users\\krzst\\keys.json"
    keys = list()
    keys = importKeys(path)
    print(keys)

if __name__=="__main__":
    main()