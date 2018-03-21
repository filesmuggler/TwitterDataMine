import wx
import os

class ConfigureStep(wx.Frame):

    def __init__(self, *args, **kw):
        super(ConfigureStep,self).__init__(*args,**kw)
        pnl = wx.Panel(self)
        pnl.SetBackgroundColour(wx.Colour(29, 202, 255, 255))
        st = wx.StaticText(pnl,label="Configure Step",pos=(25,20))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)
        st.SetForegroundColour("WHITE")


        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText("Please fill in credentials")

        
        self.path_label = wx.StaticText(pnl, label="Path to local key store:",pos=(25,70))
        self.path_label.SetForegroundColour("WHITE")
        self.path = wx.TextCtrl(pnl, size=(140, -1),pos=(150,70))

        self.ck_label = wx.StaticText(pnl, label="Customer key:",pos=(25,100))
        self.ck_label.SetForegroundColour("WHITE")
        self.ck = wx.TextCtrl(pnl, size=(140, -1),pos=(150,100))

        self.cs_label = wx.StaticText(pnl, label="Customer secret:",pos=(25,130))
        self.cs_label.SetForegroundColour("WHITE")
        self.cs = wx.TextCtrl(pnl, size=(140, -1),pos=(150,130))

        self.at_label = wx.StaticText(pnl, label="Access token:",pos=(25,160))
        self.at_label.SetForegroundColour("WHITE")
        self.at = wx.TextCtrl(pnl, size=(140, -1),pos=(150,160))

        self.ats_label = wx.StaticText(pnl, label="Access secret:",pos=(25,190))
        self.ats_label.SetForegroundColour("WHITE")
        self.ats = wx.TextCtrl(pnl, size=(140, -1),pos=(150,190))

        self.save_button = wx.Button(pnl, label="Save",pos=(320,190))
        self.Bind(wx.EVT_BUTTON, self.OnSave, self.save_button)

        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(pnl, 1, wx.ALL | wx.EXPAND)

    def makeMenuBar(self):
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
        exitItem = helpMenu.Append(wx.ID_EXIT)

        menuBar = wx.MenuBar()
        menuBar.Append(helpMenu,'&Help')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)

    def OnExit(self, event):
        self.Close(True)

    def OnAbout(self, event):
        wx.MessageBox("Application for Filtering data from Twitter\nVersion 0.0.1 ","About",wx.OK|wx.ICON_INFORMATION)

    def OnSave(self, event):
        path_p = self.path.GetValue()
        path_f = ''
        for letter in path_p:
            path_f = path_f + letter
            if letter == '\\':
                path_f = path_f + '\\'

        f = open(path_f,'w')
        f.write(self.ck.GetValue()+"\n")
        f.write(self.cs.GetValue()+"\n")
        f.write(self.at.GetValue()+"\n")
        f.write(self.ats.GetValue()+"\n")

        path_c = os.getcwd() + "\\config_file.txt"
        g = open(path_c,'w')
        g.write(path_f)

        self.Close(True)

   # def GetData(parent=None, message='', default_value=''):
    #    dlg = 

        