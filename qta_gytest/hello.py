# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2020/03/21 QTAF自动生成
from time import sleep

from qta_gylib.weixin.WXapp import WXApp
from qta_gylib.weixin.wx_basepage import GYTestBase


class HelloTest(GYTestBase):
    '''示例测试用例
    '''
    owner = "coye"
    timeout = 5
    priority = GYTestBase.EnumPriority.High
    status = GYTestBase.EnumStatus.Design
    tags= "test_eg"
    
    def run_test(self):
        acc=""
        pwd=""
        device = self.acquire_device()
        app = WXApp(device)
        app.login(acc, pwd)
    
if __name__ == '__main__':
    HelloTest().debug_run()

