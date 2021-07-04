# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:12
# @Author  : wkRonin
# @File    :basepage.py
import logging

import allure
from appium import webdriver


# 页面基类
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


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
            logging.info("实例化driver")
        else:
            self.driver = driver_base

    def uiauto_find(self, locator):
        ele = self.driver.find_element_by_android_uiautomator(locator)
        return ele

    def get_toast(self,  locator, by=MobileBy.XPATH, timeout=10):
        # toast展示2-3秒自动消失，使用find_element会在隐式等待的时间内查找
        # element: WebElement = WebDriverWait(self.driver, timeout).until(
        #     lambda x: x.find_element(by, locator)
        # )
        element = self.find(by, locator)
        toast_text = element.text
        return toast_text

    def find(self, by, locator):
        ele = self.driver.find_element(by, locator)
        return ele

    def save_screenshot(self, path, stepname):
        """
        allure报告截图步骤
        :param path: 截图保存的路径
        :param stepname: 步骤名称
        :return:
        """
        with allure.step(stepname):
            self.driver.save_screenshot(path)
            allure.attach.file(path, stepname)

    def swipe_find(self, text, num=4):
        """

        :param text:xpath使用的文本
        :param num:滑动的次数
        :return:找到的元素
        """
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                element = self.find(MobileBy.XPATH, f"//*[@text='{text}']").click()
                self.driver.implicitly_wait(5)
                return element
            except:
                logging.info("未找到")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']

                start_x = width/2
                start_y = height*0.8
                end_x = start_x
                end_y = height*0.3
                duration = 2000

                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

            if i == num-1:

                raise NoSuchElementException(f'找了{i}次，未找到')
