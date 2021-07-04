# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 17:06
# @Author  : wkRonin
# @File    :app.py
import logging

from appium import webdriver

from homework0701.po.basepage import BasePage
from homework0701.po.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            logging.info("driver == None 创建driver")
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "hogwarts"
            caps["noReset"] = "true"
            # 提升 启动app速度的配置
            caps['skipDeviceInitialization'] = "true"
            caps['udid'] = 'd59c99c6'
            # 只有 [动态页面] 才需要设置这个 时间
            # caps["settings[waitForIdleTimeout]"] = 0
            # 至关重要的一行  与appium 服务建立连接，并传递一个caps 字典对象
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 隐式等待 5s 动态的等待元素出现，如果五秒 之内都没有找到元素，就会抛异常
            # 每次调用find_element/s 方法的时候都会动态的等待
            self.driver.implicitly_wait(5)
        else:
            logging.info('driver != None 复用driver')
            self.driver.launch_app()

        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        # 进入主页入口
        return MainPage(self.driver)
