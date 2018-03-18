import json
import re
import tweepy
import operator
import wx
from collections import Counter
from tweepy import OAuthHandler

from BasicFrame import BasicFrame
from ConfigureStep import ConfigureStep
from displayUserData import displayUserData
from printFromJson import printFromJson
from configureAPI import configureAPI
from collectTweets import collectTweets


def main():
    
    #configuring Twitter API
    api = configureAPI()
    
    app = wx.App()
    frm = ConfigureStep(None,title="SimpleTwitterMineData",size=(480, 320)).Show()
    app.MainLoop()
    
    
if __name__=="__main__":
    main()