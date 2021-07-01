# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 22:56
# @Author  : wkRonin
# @File    :class_1st.py
from time import sleep

from appium import webdriver
desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = '192.168.80.102:5555'
# com.android.settings/com.android.settings.Settings
# 打开手机设置页
# desired_caps['appPackage']='com.android.settings'
# desired_caps['appActivity']='com.android.settings.Settings'
# 打开雪球首页
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'view.WelcomeActivityAlias'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print("启动【设置】应用")
sleep(5)
driver.quit()
