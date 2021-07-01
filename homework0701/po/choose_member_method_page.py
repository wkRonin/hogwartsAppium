# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:30
# @Author  : wkRonin
# @File    :choose_member_method_page.py
from homework0701.po.add_member_page import AddMemberPage
from homework0701.po.basepage import BasePage


# 选择添加成员方式页
class ChooseMemberMethodPage(BasePage):

    def click_manual_input(self):
        # 点击手动输入添加
        # 进入编辑成员页

        return AddMemberPage(self.driver)

    def click_back(self):
        # 点击返回按钮
        # 进入通讯录页
        from homework0701.po.contact_page import ContactPage

        return ContactPage(self.driver)