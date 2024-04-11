import wx
import requests


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Currency Converter')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        self.txt_control_to = wx.TextCtrl(panel, pos=(5, 5), size=(70, -1))
        to_label = wx.StaticText(panel, id=-1, label='Convert to:', pos=(50, 5))
        my_sizer.Add(self.txt_control_to, 0, wx.ALL | wx.ALIGN_CENTER, 5)

        self.txt_control_from = wx.TextCtrl(panel, pos=(5, 50), size=(70, -1))
        from_label = wx.StaticText(panel, id=-1, label='Convert from:', pos=(50, 40))
        my_sizer.Add(self.txt_control_from, 0, wx.ALL | wx.ALIGN_CENTER, 5)

        self.txt_control_amount = wx.TextCtrl(panel, pos=(5, 80), size=(70, -1))
        amount_label = wx.StaticText(panel, id=-1, label='Amount:', pos=(50, 70))
        my_sizer.Add(self.txt_control_amount, 0, wx.ALL | wx.ALIGN_CENTER, 5)

        my_btn = wx.Button(panel, label='Convert', pos=(5, 200))
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)

        self.Show()

    def on_press(self, event):
        to_currency = self.txt_control_to.GetValue().upper()
        from_currency = self.txt_control_from.GetValue().upper()
        amount = self.txt_control_amount.GetValue().upper()

        response = requests.get(
            f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

        # print(response.status_code)

        print(
            f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
