# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:12
# @Author  : wkRonin
# @File    :basepage.py
import logging
import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


# 页面基类
class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def uiauto_find(self, locator):
        # uiautomator方法查找元素
        return self.driver.find_element_by_android_uiautomator(locator)

    def uiauto_find_and_click(self, locator):
        self.uiauto_find(locator).click()

    def get_toast(self,  locator, by=MobileBy.XPATH, timeout=10):
        # toast展示2-3秒自动消失，使用find_element会在隐式等待的时间内查找,直接用find即可，不用显示等待
        # element: WebElement = WebDriverWait(self.driver, timeout).until(
        #     lambda x: x.find_element(by, locator)
        # )
        element = self.find(by, locator)
        toast_text = element.text
        return toast_text

    def find(self, by, locator):
        # 查找元素
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        # 查找元素之后完成点击操作
        self.find(by, locator).click()

    def find_and_sendkeys(self, by, locator, value):
        self.find(by, locator).sendkeys(value)

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
        滑动查找元素并点击
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
                logging.info(f"第{i}次未找到")
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

    def back(self, num=3):
        for i in range(num):
            self.driver.back()
