import wx

class MainWindow(wx.Frame):
  
    def __init__(self, parent,ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(800, 600))

        panel1 = wx.Panel(self,-1, style=wx.BORDER_NONE)
        panel2 = wx.Panel(self,-1, style=wx.BORDER_THEME)
        panel3 = wx.Panel(self,-1, style=wx.BORDER_THEME)

        panel1.SetBackgroundColour(wx.Colour(29,202,255,0))
        panel2.SetBackgroundColour(wx.Colour(192,222,237,0))
        panel3.SetBackgroundColour(wx.Colour(255,255,255,0))

        welcomeText = wx.StaticText(panel1,label="Welcome!", style=wx.ALIGN_CENTRE)
        font = welcomeText.GetFont()
        font.PointSize += 20
        font = font.Bold()
        welcomeText.SetFont(font)
        welcomeText.SetForegroundColour("WHITE")
        
        welcomePanelSizer = wx.BoxSizer()
        welcomePanelSizer.Add(welcomeText,1)
        panel1.SetSizerAndFit(welcomePanelSizer)
        panel1.Layout()


        boxh = wx.BoxSizer(wx.HORIZONTAL)
        boxh.Add(panel2,1,wx.EXPAND)
        boxh.Add(panel3,3,wx.EXPAND)


        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel1, 1, wx.EXPAND)
        box.Add(boxh, 6, wx.EXPAND)

        self.SetAutoLayout(True)
        self.SetSizer(box)
        self.Layout()

