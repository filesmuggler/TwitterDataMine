import json
import re
import tweepy
import operator
import wx
from collections import Counter
from tweepy import OAuthHandler

from ConfigureStep import ConfigureStep
from MainWindow import MainWindow

from Analyzer import Analyzer
from Configurator import Configurator


def main():
    
    #configuring Twitter API
    #api = configureAPI()

    configurator = Configurator()
    api = configurator.returnAPI()

    #app = wx.App()
    #frm = MainWindow(None,-1,title="SimpleTwitterMineData").Show()
    #app.MainLoop()
    #collectTweets(api,"elonmusk",5)
    analyzer = Analyzer(api)
    analyzer.filterByTerm("created_at","tweets.json")


    
if __name__=="__main__":
    main()