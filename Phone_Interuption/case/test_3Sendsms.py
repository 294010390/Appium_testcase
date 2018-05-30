#coding:utf-8

import os
import unittest
from appium import webdriver

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
        desired_caps['appPackage'] = 'com.android.mms'
        desired_caps['appActivity'] = '.ui.ComposeMessageActivity'
        desired_caps["unicodeKeyboard"] = 'True'
        desired_caps["resetKeyboard"] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        #os.system('adb shell ime set com.iflytek.inputmethod.FlyIME') #恢复为讯飞输入法
        self.driver.quit()

    def test_sendsms(self):

        #编辑联系人
        s1 = self.driver.find_element_by_id("com.android.mms:id/recipients_editor")
        s1.send_keys("13262885325")

        # 返回，显示消息内容框
        #self.driver.press_keycode(4)

        # 编辑消息内容
        s2 = self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        s2.send_keys(u'Hello World,你好，Appium')

        #发送
        self.driver.find_element_by_id("com.android.mms:id/send_button_sms").click()
