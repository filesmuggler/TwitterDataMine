import wx

class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainWindow,self).__init__(*args,**kw)
       
        #pnl = wx.Panel(self)
        #st = wx.StaticText(pnl, label="Welcome!", pos=(10,10))
        #font = st.GetFont()
        #font.PointSize += 10
        #font = font.Bold()
        #st.SetFont(font)
        #self.hline = wx.StaticLine(pnl, 1, (20,60), (740,3), style=wx.LI_HORIZONTAL)

        welcomePanel = wx.Panel(self,1,style=wx.BORDER_NONE)
        welcomePanel.SetBackgroundColour(wx.Colour(0,132,180,0))
        st = wx.StaticText(welcomePanel, label="Welcome!", pos=(10,10))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)
        st.SetForegroundColour(wx.Colour(255,255,255,255))

        self.hline = wx.StaticLine(welcomePanel, 1, (20,60), (740,3), style=wx.LI_HORIZONTAL)
        self.hline.SetForegroundColour(wx.Colour(192,222,237,255))

        workingPanel = wx.Panel(self,1,style=wx.BORDER_NONE)
        workingPanel.SetBackgroundColour(wx.Colour(255,255,255,0))

        self.box = wx.BoxSizer(wx.VERTICAL)
        self.box.Add(welcomePanel,0.5,wx.EXPAND)
        self.box.Add(self.hline,0.2,wx.EXPAND)
        self.box.Add(workingPanel,3,wx.EXPAND)
        
        self.SetAutoLayout(True)
        self.SetSizer(self.box)
        self.Layout()
