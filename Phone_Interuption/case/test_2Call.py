#coding:utf-8

import os
import unittest
from appium import webdriver
from time import sleep
from Clientnew import ClientTransmit

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class test2(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'WTKDU16903013283'  # Honor8
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.DialtactsActivity'
        desired_caps["unicodeKeyboard"] = 'True'
        desired_caps["resetKeyboard"] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        #os.system('adb shell ime set com.iflytek.inputmethod.FlyIME') #恢复为讯飞输入法
        self.driver.quit()

    def test_call(self):

        num1 = self.driver.find_element_by_name("1")
        num0 = self.driver.find_element_by_name("0")

        #Call 10010
        num1.click()
        num0.click()
        num0.click()
        num1.click()
        num0.click()

        # dial the call
        self.driver.find_element_by_id("com.android.contacts:id/dialButton").click()
        sleep(4)
        newT = ClientTransmit()
        newT.CLSend(1)
        sleep(10)
        newT.CLSend(2)
        sleep(2)

        self.driver.find_element_by_id("com.android.incallui:id/endButton").click()