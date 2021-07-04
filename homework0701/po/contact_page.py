# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:21
# @Author  : wkRonin
# @File    :contact_page.py
import logging
import time

import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.po.basepage import BasePage
from homework0701.po.choose_member_method_page import ChooseMemberMethodPage


# 通讯录页
from homework0701.po.contact_detail_brief_page import ContactDetailBriefPage
from homework0701.po.contact_search_page import ContactSearchPage


class ContactPage(BasePage):

    _addmember_element = '添加成员'
    _search_element = (MobileBy.ID, 'com.tencent.wework:id/hci')

    def click_add_member(self):
        # 点击添加成员
        # 进入选择添加成员方式页

        with allure.step('点击添加成员'):
            # self.find(MobileBy.ANDROID_UIAUTOMATOR,
            #           'new UiScrollable(new UiSelector().scrollable(true).\
            #           instance(0)).scrollIntoView(new UiSelector().\
            #           text("添加成员").instance(0));').click()
            self.swipe_find(self._addmember_element)
            logging.info('点击添加成员')
        return ChooseMemberMethodPage(self.driver)

    def click_member_name(self, name):
        # 点击人员名字
        # 进入人员的个人信息简单页
        with allure.step('点击人员姓名'):
            self.swipe_find(name)
            logging.info('点击人员姓名')
        return ContactDetailBriefPage(self.driver)

    def click_search(self):
        # 点击查询按钮
        # 进入查询页
        with allure.step('点击通讯录的查询按钮'):
            self.find_and_click(*self._search_element)
            logging.info('点击通讯录的查询按钮')
        return ContactSearchPage(self.driver)


