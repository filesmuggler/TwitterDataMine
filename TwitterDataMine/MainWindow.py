import wx

class MainWindow(wx.Frame):
  
    def __init__(self, parent,ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(300, 250))

        panel1 = wx.Panel(self,-1, style=wx.SUNKEN_BORDER)
        panel2 = wx.Panel(self,-1, style=wx.SUNKEN_BORDER)
        panel3 = wx.Panel(self,-1, style=wx.SUNKEN_BORDER)

        panel1.SetBackgroundColour("BLUE")
        panel2.SetBackgroundColour("RED")
        panel3.SetBackgroundColour("GREEN")

        boxh = wx.BoxSizer(wx.HORIZONTAL)
        boxh.Add(panel2,1,wx.EXPAND)
        boxh.Add(panel3,1,wx.EXPAND)


        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel1, 1, wx.EXPAND)
        box.Add(boxh, 5, wx.EXPAND)

        self.SetAutoLayout(True)
        self.SetSizer(box)
        self.Layout()

