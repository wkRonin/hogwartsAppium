# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:21
# @Author  : wkRonin
# @File    :contact_page.py
import logging

import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.po.basepage import BasePage
from homework0701.po.choose_member_method_page import ChooseMemberMethodPage


# 通讯录页
class ContactPage(BasePage):

    def click_add_member(self):
        # 点击添加成员
        # 进入选择添加成员方式页
        with allure.step('点击添加成员'):
            # self.find(MobileBy.ANDROID_UIAUTOMATOR,
            #           'new UiScrollable(new UiSelector().scrollable(true).\
            #           instance(0)).scrollIntoView(new UiSelector().\
            #           text("添加成员").instance(0));').click()
            self.swipe_find('添加成员')
            logging.info('点击添加成员')
        return ChooseMemberMethodPage(self.driver)

