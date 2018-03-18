import json
import re
import tweepy
import operator
import wx
from collections import Counter
from tweepy import OAuthHandler

from BasicFrame import BasicFrame
from displayUserData import displayUserData
from printFromJson import printFromJson
from configureAPI import configureAPI
from collectTweets import collectTweets


def main():
    
    


    #configuring Twitter API
    api = configureAPI()

    #targeting user
    target = 'chris_stezala09'
    number = 5
    collectTweets(api, target, number)

    app = wx.App()
    frm = BasicFrame(None,title="Hello Python!").Show()
    app.MainLoop()
    
    
if __name__=="__main__":
    main()