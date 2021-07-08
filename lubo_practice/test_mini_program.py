# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 0:02
# @Author  : wkRonin
# @File    :test_mini_program.py
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebview:
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '8.0',
            # 'browserName': '',
            'noReset': 'true',
            'newCommandTimeout': '300',
            'showChromedriverLog': 'true',
            'deviceName': 'com.tecent.mm',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'unicodeKeyboard': 'true',
            'resetKeyvoard': 'true',
            'chromeOptions': {'w3c': False,
                              'androidProcess': 'com.tencent.mm:appbrand0'
                              },
            'udid': 'd59c99c6',
            # 'chromedriverExecutableDir': r'D:\pycharmproject\pythonProject\hogwartsAppium\chromedrivers'
            # 'chromedriverChromeMappingFile': 'D:\pycharmproject\pythonProject\hogwartsAppium\mapping.json',
            # 通过自己的adb代理修复chromedriver的bug并解决@xweb_devtools_remote的问题
            # 'adbPort': 5038
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")
        # self.driver.implicitly_wait(10)


    def teardown(self):
        self.driver.quit()

    def find_top_window(self):
        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                print(self.driver.title)
                return True
            else:
                self.driver.switch_to.window(window)
        return False

    def test_search(self):
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width'] * 0.5, size['height'] * 0.8)
        sleep(5)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索小程序']").click()
        sleep(5)
        print(self.driver.contexts)
        # self.driver.switch_to.context("WEBVIEW_com.tencent.mm:toolsmp")
        # self.find_top_window()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable((MobileBy.XPATH, "//*[@text='取消']")))
        self.driver.find_element(MobileBy.ID, 'com.tencent.mm:id/db_').send_keys("雪球")
        sleep(5)