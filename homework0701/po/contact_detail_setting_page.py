# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 19:29
# @Author  : wkRonin
# @File    :contact_detail_setting_page.py
import logging

import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.po.basepage import BasePage
from homework0701.po.contact_edit_page import ContactEditPage


class ContactDetailSettingPage(BasePage):

    _edit_button = (MobileBy.ID, 'com.tencent.wework:id/b5r')

    def click_edit_member(self):
        # 点击编辑成员按钮
        # 进入人员编辑页
        with allure.step('点击编辑成员按钮'):
            self.find_and_click(*self._edit_button)
            logging.info('点击编辑成员按钮')
        return ContactEditPage(self.driver)