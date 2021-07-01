# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:10
# @Author  : wkRonin
# @File    :test_add_member.py
from homework0701.po.main_page import MainPage


class TestAddMember:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    def test_add_member(self):
        self.main.goto_contact().click_add_member().click_manual_input().\
            edit_member().click_back().get_member_name()


