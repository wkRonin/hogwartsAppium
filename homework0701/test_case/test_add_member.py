# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:10
# @Author  : wkRonin
# @File    :test_add_member.py
import allure
import pytest
from faker import Faker

from homework0701.po.app import App
from homework0701.po.main_page import MainPage

@allure.feature('企业微信app测试')
@allure.story('通讯录测试')
class TestAddMember:

    def setup_class(self):
        self.fake = Faker('zh_CN')
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back(5)

    def teardown_class(self):
        self.app.quit()

    @allure.title('添加成员')
    def test_add_member(self):
        name = self.fake.name()
        phone = self.fake.phone_number()
        result = self.main.goto_contact().click_add_member().click_manual_input().\
            edit_member(name, phone).get_toast_text()
        self.main.save_screenshot('../img/addsuccess0704.png', '添加成员成功截图')
        assert result == '添加成功'


