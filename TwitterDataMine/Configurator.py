import tweepy
import json
import os
import sys
import wx
from tweepy import OAuthHandler
from DialogBox import DialogBox
from ConfigureStep import ConfigureStep

class Configurator():
    __slots__ = ['api']
    def __init__(self):
        path = os.getcwd()+"\\config_file.txt"
        self.__isFirst(path)
        keys = []
        keys = self.__importKeys(path)

        consumer_key = keys[0]
        consumer_secret = keys[1]
        access_token = keys[2]
        access_secret = keys[3]
        
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        self.api = tweepy.API(auth) 

    def __isFirst(self,path):
        if(os.path.isfile(path)):
            return True
        else:
            app = wx.App()
            frm = ConfigureStep(None,title="SimpleTwitterMineData",size=(480, 320)).Show()
            app.MainLoop()

    def __importKeys(self,path_p):
        keys = []
        path_f = ''
        with open(path_p,'r') as f:
            for line in f:
                for letter in line:
                    path_f = path_f + letter
                    if letter == '\\':
                        path_f = path_f + '\\'
        
        try:
            with open(path_f, 'r') as g:
                for line in g:
                    line = line[:-1]
                    keys.append(line)
            return keys
        except IOError:
        # not elegant of signalising the error
            dlg = wx.App()
            DialogBox()
            dlg.MainLoop()


    def returnAPI(self):
        return self.api