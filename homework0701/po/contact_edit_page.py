# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 19:36
# @Author  : wkRonin
# @File    :contact_edit_page.py
import logging

import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.po.basepage import BasePage



class ContactEditPage(BasePage):

    _delete_member_button = '删除成员'
    _confirm_button = (MobileBy.ID, 'com.tencent.wework:id/bg8')

    def click_delete_member(self):
        # 点击删除成员按钮
        # 点击确定
        # 返回通讯录页
        from homework0701.po.contact_page import ContactPage
        with allure.step('点击删除成员按钮'):
            self.swipe_find(self._delete_member_button)
            logging.info('点击删除成员按钮')
        with allure.step('点击确定按钮'):
            self.find_and_click(*self._confirm_button)
            logging.info('点击确定按钮')
        return ContactPage(self.driver)