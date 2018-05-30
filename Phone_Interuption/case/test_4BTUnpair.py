#coding:utf-8

import os
import unittest
from appium import webdriver
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class PhoneAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'WTKDU16903013283'  # Honor8
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings$BluetoothSettingsActivity'
        desired_caps["unicodeKeyboard"] = 'True'
        desired_caps["resetKeyboard"] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def tearDown(self):
        #os.system('adb shell ime set com.iflytek.inputmethod.FlyIME') #恢复为讯飞输入法
        self.driver.quit()

    def test_unpair(self):

        devicename = u'妖怪'

        if (devicename in self.driver.page_source):
        # if (self.driver.find_element_by_name(u"妖怪").is_displayed() == False):
        #     raise NameError(u"指定设备未连接")

            s0 = self.driver.find_element_by_id("com.android.settings:id/konw_more")
            s0.click()

            s1 = self.driver.find_element_by_id("androidhwext:id/preference_emui_description_container")
            s1.click()
        else:
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            pic_path = ".\\screenshot\\"
            picname = 'screenshot' + timestamp + '.png'
            pic = pic_path + picname
            self.driver.get_screenshot_as_file(pic)
            raise NameError(u"指定设备未连接"+u"ScreenShot:"+picname)
