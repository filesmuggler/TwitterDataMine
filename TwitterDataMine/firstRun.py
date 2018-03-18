import os
import wx
from ConfigureStep import ConfigureStep

def firstRun(path):
    #check if file with keys exists
    #if not create one and ask for keys
    if(os.path.isfile(path)):
        return True
    else:
        # connect window with path and passing keys
        app = wx.App()
        frm = ConfigureStep(None,title="SimpleTwitterMineData",size=(480, 320)).Show()
        app.MainLoop()


    
    

   
