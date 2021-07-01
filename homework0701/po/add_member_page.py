# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:34
# @Author  : wkRonin
# @File    :add_member_page.py
from homework0701.po.basepage import BasePage


# 编辑成员页
class AddMemberPage(BasePage):

    def edit_member(self):
        # 编辑成员信息
        # 保存后进入选择添加成员方式页
        from homework0701.po.choose_member_method_page import ChooseMemberMethodPage

        return ChooseMemberMethodPage(self.driver)