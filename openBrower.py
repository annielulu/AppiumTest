# coding:utf-8
__author__ = 'annie'

from selenium import webdriver
import time

def startBrowser():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.maximize_window()
    time.sleep(5)
    driver.close()

startBrowser()