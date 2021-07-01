# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:13
# @Author  : wkRonin
# @File    :main_page.py
from homework0701.po.basepage import BasePage
from homework0701.po.contact_page import ContactPage


# 企业微信首页
class MainPage(BasePage):

    def goto_contact(self):
        # 点击通讯录
        # 进入通讯录页
        return ContactPage(self.driver)
