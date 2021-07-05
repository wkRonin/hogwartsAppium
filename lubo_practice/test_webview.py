# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 22:29
# @Author  : wkRonin
# @File    :test_webview.py
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebview:
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '8.0',
            'browserName': 'Chrome',
            'noReset': 'true',
            # 'skipDeviceInitialization': 'true',
            'deviceName': '456456',
            'chromeOptions': {'w3c': False
                              # ,'args': ['--no-sandbox']
                              },
            'udid': 'emulator-5554',
            'chromedriverExecutable': 'D:\pycharmproject\pythonProject\hogwartsAppium\chromedriver67_69\chromedriver.exe'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.get('http://m.baidu.com')
        # 中部弹窗是安卓原生的，底部弹窗才是alert.
        # 解决安卓谷歌浏览器位置权限弹窗
        self.driver.switch_to.context("NATIVE_APP")
        WebDriverWait(self.driver, 10, 0.5).until(
            expected_conditions.visibility_of_element_located((MobileBy.XPATH, "//*[@text='允许']"))).click()
        # 切换回浏览器
        webview = self.driver.contexts[1]
        self.driver.switch_to.context(webview)
        # 查询操作
        self.driver.find_element(MobileBy.ID, 'index-kw').send_keys('appium')
        search = WebDriverWait(self.driver, 10, 0.5).until(
            expected_conditions.visibility_of_element_located((MobileBy.ID, 'index-bn'))
        )
        search.click()

        sleep(8)