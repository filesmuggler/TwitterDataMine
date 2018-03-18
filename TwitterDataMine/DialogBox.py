import wx
import sys

class DialogBox(wx.Frame):
    def __init__(self, *args, **kw):
        super(DialogBox,self).__init__(*args,**kw)
        wx.MessageBox("Oops! Remove config.txt and restart app","Exception",wx.OK|wx.ICON_STOP)
        self.Close(True)
        sys.exit()

        
        