# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:12
# @Author  : wkRonin
# @File    :basepage.py
import logging

from appium import webdriver

# 页面基类
class BasePage:

    def __init__(self, driver_base: webdriver = None):
        if driver_base is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "hogwarts"
            caps["noReset"] = "true"
            # 提升 启动app速度的配置
            caps['skipDeviceInitialization'] = "true"
            # 只有 [动态页面] 才需要设置这个 时间
            # caps["settings[waitForIdleTimeout]"] = 0
            # 至关重要的一行  与appium 服务建立连接，并传递一个caps 字典对象
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 隐式等待 5s 动态的等待元素出现，如果五秒 之内都没有找到元素，就会抛异常
            # 每次调用find_element/s 方法的时候都会动态的等待
            self.driver.implicitly_wait(5)
            print("实例化driver")
        else:
            self.driver = driver_base
