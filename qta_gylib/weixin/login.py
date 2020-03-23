from qt4a.andrcontrols import Window, Button, EditText
from qt4a.qpath import QPath


class LoginPanel(Window):
    '''登录界面
    '''
    Activity = ' com.tencent.mm/com.tencent.mm.plugin.account.ui.WelcomeActivity'  # 登录界面

    def __init__(self, demoapp):
        super(LoginPanel, self).__init__(demoapp)
        LoginPanel.Activity=self.device.get_current_activity()
        self.update_locator({'登录': {'type': Button, 'root': self, 'locator': QPath('/Id="f34"')},
                             })

    def login(self):
        '''登录界面
        '''
        self.wait_for_exist()
        self.Controls["登录"].click()
    def login_phone(self,acc, pwd):
        LoginPanel.Activity="com.tencent.mm.plugin.account.ui.MobileInputUI"
        self.update_locator({'手机号': {'type': EditText, 'root': self, 'locator': QPath('/Id="bem"')},
                             '下一步': {'type': Button, 'root': self, 'locator': QPath('/Id="dw1"')},
                             '我知道了': {'type': Button, 'root': self, 'locator': QPath('/Id="dj6"')},
                             '密码': {'type': EditText, 'root': self, 'locator': QPath('/Id="f5b" /Id="bem"')},
                             '登录': {'type': Button, 'root': self, 'locator': QPath('/Id="dw1"')},
                             })
        self.Controls["手机号"].text = acc
        self.Controls["下一步"].click()
        if self.Controls["我知道了"].wait_for_exist():
            self.Controls["我知道了"].click()
        self.Controls["手机号"].text = pwd
        self.Controls["下一步"].click()
