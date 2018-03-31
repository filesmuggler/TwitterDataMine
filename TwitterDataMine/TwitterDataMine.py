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
    configurator = Configurator()
    api = configurator.returnAPI()

    analyzer = Analyzer(api)
    analyzer.mostFrequent("elonmusk",100,"text","elonmusk10.json",True)

    #app = wx.App()
    #frm = MainWindow(None,-1,title="SimpleTwitterMineData").Show()
    #app.MainLoop
    


    
if __name__=="__main__":
    main()