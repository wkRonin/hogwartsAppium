# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 22:01
# @Author  : wkRonin
# @File    :test_luzhi.py
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# pip install appium-python-client
import time

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["deviceName"] = "hogwarts"
caps["noReset"] = "true"
# 至关重要的一行  与appium 服务建立连接，并传递一个caps 字典对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
time.sleep(5)
el1 = driver.find_element_by_xpath("//*[@text='通讯录']")
el1.click()
time.sleep(3)
el2 = driver.find_element_by_id("com.tencent.wework:id/hci")
el2.click()
time.sleep(3)
el3 = driver.find_element_by_id("com.tencent.wework:id/g5f")
el3.send_keys("朱维康")
el4 = driver.find_element_by_id("com.tencent.wework:id/d_1")
el4.click()


driver.quit()
