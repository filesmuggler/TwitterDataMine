import wx

class ConfigureStep(wx.Frame):

    def __init__(self, *args, **kw):
        super(ConfigureStep,self).__init__(*args,**kw)
        pnl = wx.Panel(self)
        st = wx.StaticText(pnl,label="Configure Step",pos=(25,20))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)


        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText("Please fill in credentials")

        
        self.lblname = wx.StaticText(pnl, label="Customer key:",pos=(25,70))
        self.editname = wx.TextCtrl(pnl, size=(140, -1),pos=(120,70))
        self.lblname = wx.StaticText(pnl, label="Customer secret:",pos=(25,100))
        self.editname = wx.TextCtrl(pnl, size=(140, -1),pos=(120,100))
        self.lblname = wx.StaticText(pnl, label="Access token:",pos=(25,130))
        self.editname = wx.TextCtrl(pnl, size=(140, -1),pos=(120,130))
        self.lblname = wx.StaticText(pnl, label="Access secret:",pos=(25,160))
        self.editname = wx.TextCtrl(pnl, size=(140, -1),pos=(120,160))

        self.button = wx.Button(pnl, label="Save",pos=(25,200))

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
