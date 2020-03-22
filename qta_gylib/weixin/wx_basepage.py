from qt4a.androidtestbase import AndroidTestBase
from qt4a.device import Device
from qt4a.androiddriver.util import logger

class GYTestBase(AndroidTestBase):
    '''demo测试用例基类
    '''

    def post_test(self):
        '''清理测试用例
        '''

        logger.info('开始执行测试清理。。。')
        super(GYTestBase, self).post_test()
        Device.release_all_device()  # 释放所有设备
        logger.info('测试清理执行完毕。')

    def acquire_device(self, type='Android', device_id='', **kwds):
        '''申请设备

        :param type: 申请的设备类型，目前尚未使用
        :type type:  string
        :param device_id: 申请的设备ID，默认不指定设备ID
        :type device_id:  string
        '''
        logger.info('开始申请设备。。。')
        device = super(GYTestBase, self).acquire_device(device_id, **kwds)
        device.adb.start_logcat([])
        logger.info('设备名称%s' % str(device.device_list))
        return device