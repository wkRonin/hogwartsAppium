# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 18:33
# @Author  : wkRonin
# @File    :test_delete_member.py
import allure
from faker import Faker

from homework0701.po.app import App


@allure.feature('企业微信app测试')
@allure.story('通讯录测试')
class TestAddMember:

    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back(5)

    def teardown_class(self):
        self.app.quit()

    @allure.title('删除成员')
    def test_delete_member(self):
        result = self.main.goto_contact().click_member_name('姜久').click_set().click_edit_member().\
            click_delete_member().click_search().get_search_result('姜久')
        self.main.save_screenshot('../img/deletesuccess0704.png', '查询无结果截图')
        assert result == 0
