# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 19:14
# @Author  : wkRonin
# @File    :contact_detail_brief_page.py
import logging

import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.po.basepage import BasePage


# 个人信息简单页
from homework0701.po.contact_detail_setting_page import ContactDetailSettingPage


class ContactDetailBriefPage(BasePage):

    _set_button = (MobileBy.ID, 'com.tencent.wework:id/hc9')

    def click_set(self):
        # 点击右上角的设置按钮
        # 进入人员详情设置页
        with allure.step('点击设置按钮'):
            self.find_and_click(*self._set_button)
            logging.info('点击设置按钮')
        return ContactDetailSettingPage(self.driver)