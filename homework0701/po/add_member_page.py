# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:34
# @Author  : wkRonin
# @File    :add_member_page.py
import logging

import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.po.basepage import BasePage


# 编辑成员页
class AddMemberPage(BasePage):

    _inputname_element = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText")
    _inputphone_element = 'new UiSelector().resourceId("com.tencent.wework:id/f7y")'

    def edit_member(self, name, phone):
        # 编辑成员信息
        # 保存后进入选择添加成员方式页
        from homework0701.po.choose_member_method_page import ChooseMemberMethodPage
        with allure.step('编辑成员信息'):
            # 输入姓名
            # self.uiauto_find('new UiSelector().resourceId("com.tencent.wework:id/b09").instance(0)').send_keys(name)
            # 和姓名是兄弟节点关系，用父节点去找兄弟节点
            self.find(*self._inputname_element).send_keys(name)
            logging.info(f'输入姓名：{name}')
            # 输入手机号
            self.uiauto_find(self._inputphone_element).send_keys(phone)
            logging.info(f'输入手机号：{phone}')
        with allure.step('点击保存'):
            # 点击保存
            # self.find(MobileBy.ANDROID_UIAUTOMATOR,
            #           'new UiScrollable(new UiSelector().scrollable(true).\
            #           instance(0)).scrollIntoView(new UiSelector().\
            #           text("保存").instance(0));').click()
            self.swipe_find("保存")
            logging.info('点击保存')
        return ChooseMemberMethodPage(self.driver)
