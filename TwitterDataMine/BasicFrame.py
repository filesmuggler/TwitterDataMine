import wx 

class BasicFrame(wx.Frame):
    
    def __init__(self, *args, **kw):
        super(BasicFrame,self).__init__(*args,**kw)
        pnl = wx.Panel(self)
        st = wx.StaticText(pnl,label="Twitter Data Mine", pos=(25,25))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText("Welcom to wxPython!")

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1,"&Hello...\tCtrl-H","Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()

        exitItem = fileMenu.Append(wx.ID_EXIT)
        
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu,'&File')
        menuBar.Append(helpMenu,'&Help')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        self.Close(True)

    def OnHello(self, event):
        wx.MessageBox("Hello there")

    def OnAbout(self, event):
        wx.MessageBox("About","General Kenobi!",wx.OK|wx.ICON_INFORMATION)



