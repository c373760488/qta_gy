# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2020/03/21 QTAF自动生成

from qta_gylib.testcase import Qta_gyTestCase

class HelloTest(Qta_gyTestCase):
    '''示例测试用例
    '''
    owner = "coye"
    timeout = 5
    priority = Qta_gyTestCase.EnumPriority.High
    status = Qta_gyTestCase.EnumStatus.Design
    tags= "test_eg"
    
    def run_test(self):
        app=Qta_gyTestCase()
        app.login()
    
if __name__ == '__main__':
    HelloTest().debug_run()

