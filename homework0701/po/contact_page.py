# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:21
# @Author  : wkRonin
# @File    :contact_page.py
from homework0701.po.basepage import BasePage
from homework0701.po.choose_member_method_page import ChooseMemberMethodPage


# 通讯录页
class ContactPage(BasePage):

    def click_add_member(self):
        # 点击添加成员
        # 进入选择添加成员方式页
        return ChooseMemberMethodPage(self.driver)

    def get_member_name(self):
        # 获取通讯录页的名字列表
        name_list = []

        return name_list
