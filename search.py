# coding:utf-8
__author__ = 'annie'

# 引入appium包(webdriver有appium提供的所有api接口)
from appium import webdriver
def startUp():
    desired_caps ={
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "platformVersion": "4.4.2",
        # "app": "D:\\jinritoutiao5.9.5_anfensi.com.apk",
        "appPackage": "com.ss.android.article.news",
        "appActivity": "com.ss.android.article.news.activity.SplashActivity",
        "noReset": True
        # "unicodeKeyboard": True,
        # "resetKeyboard": True
    }
    # https://github.com/annielulu/DailyExercises.git
    # 实例化
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)
    # 清除搜索输入框
    driver.find_element_by_id("com.ss.android.article.news:id/bam").clear()
    print('clear')
    # 输入要搜索的内容
    driver.find_element_by_id("com.ss.android.article.news:id/bam").send_keys("name")
    print('send_keys')
    # 点击搜索
    driver.find_element_by_id("com.ss.android.article.news:id/uv").click()
    print('click')
startUp()
