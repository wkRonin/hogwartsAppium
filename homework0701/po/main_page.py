# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:13
# @Author  : wkRonin
# @File    :main_page.py
import logging

import allure

from homework0701.po.basepage import BasePage
from homework0701.po.contact_page import ContactPage


# 企业微信首页
class MainPage(BasePage):

    _addresslist_element = 'new UiSelector().resourceId("com.tencent.wework:id/e0y").text("通讯录")'

    def goto_contact(self):
        # 点击通讯录
        # 进入通讯录页

        with allure.step('点击通讯录'):
            self.uiauto_find_and_click(self._addresslist_element)
            logging.info('点击通讯录进入通讯录页')
        return ContactPage(self.driver)
