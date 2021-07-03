# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:10
# @Author  : wkRonin
# @File    :test_add_member.py
import allure
import pytest

from homework0701.po.main_page import MainPage


@allure.feature('企业微信app测试')
@allure.story('通讯录测试')
class TestAddMember:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    @allure.title('添加成员')
    @pytest.mark.parametrize("name,phone", [
        ("姜二", "13836542585")
    ])
    def test_add_member(self, name, phone):
        result = self.main.goto_contact().click_add_member().click_manual_input().\
            edit_member(name, phone).get_toast_text()
        self.main.save_screenshot('../img/addsuccess.png', '添加成员成功截图')
        assert result == '添加成功'


