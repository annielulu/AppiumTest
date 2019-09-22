# coding:utf-8
__author__ = 'annie'



from appium import webdriver
import time,os

class Driver(object):

    def startup(self):
        print('启动app')

        desired_caps = {

            "deviceName": "emulator-5554",
            "platformName": "Android",
            "platformVersion": "4.4.2",
            # "app": "D:\\jinritoutiao5.9.5_anfensi.com.apk",
            "appPackage": "com.ss.android.article.lite",
            "appActivity": "com.ss.android.article.lite.activity.SplashActivity",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True

        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        print('已经启动，等待6s中。。。')

        time.sleep(6)
        print('等待6s完成')
        return self.driver


if __name__ == '__main__':
    d = Driver()
    d.startup()

