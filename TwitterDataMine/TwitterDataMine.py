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
from MainWindow import MainWindow


def main():
    
    #configuring Twitter API
    api = configureAPI()
    app = wx.App()
    frm = MainWindow(None,-1,title="SimpleTwitterMineData").Show()
    app.MainLoop()
    #collectTweets(api,"elonmusk",5)
    
    
if __name__=="__main__":
    main()