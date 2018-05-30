#coding:utf-8

import os
import unittest
from appium import webdriver
import time
from time import sleep

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

    def test_pair(self):

        devicename = u'妖怪'

        #判断蓝牙开关
        s = self.driver.find_element_by_id('android:id/switch_widget')
        if s.get_attribute('checked') == 'false':
            s.click()
        else:
            pass

        #每次搜索到设备的id
        #self.driver.find_elements_by_id('androidhwext:id/preference_emui_content')

        pairflag = 0
        j = 0
        while (j<1 and pairflag == 0):
            i = 0
            while (i < 5):

                if (devicename in self.driver.page_source):
                    self.driver.find_element_by_name(devicename).click()
                    break
                else:
                    i = i + 1
                    continue
            if(i<5):

                sleep(5)  # 必须要足够的时间，手机才能发出请求

                ss = self.driver.find_elements_by_class_name("android.widget.Button")
                for ii in ss:
                    if ii.text == u"知道了":
                        self.driver.find_element_by_name('知道了').click()
                        j = j + 1
                        break
                    elif ii.text == u'配对':
                        s3 = self.driver.find_element_by_id('com.android.settings:id/phonebook_sharing_message_confirm_pin')
                        if s3.get_attribute('checked') == 'false':
                            s3.click()
                        else:
                            pass

                        sleep(1)

                        s2 = self.driver.find_element_by_name('配对')
                        s2.click()
                        sleep(5)
                        pairflag = 1
                        break
            else:
                # 搜索失败后抛出异常
                timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
                pic_path = ".\\screenshot\\"
                picname = 'screenshot' + timestamp + '.png'
                pic = pic_path + picname
                self.driver.get_screenshot_as_file(pic)
                raise ValueError(u"连接失败：未找到设备。"+u"ScreenShot:"+picname)
                break

        # 1连接失败后抛出异常
        if (pairflag == 0):

            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            pic_path = ".\\screenshot\\"
            picname = 'screenshot'+timestamp + '.png'
            pic = pic_path+picname
            self.driver.get_screenshot_as_file(pic)
            raise ValueError(u"连接失败：未连接"+u"ScreenShot:"+picname)