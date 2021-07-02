# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 23:30
# @Author  : wkRonin
# @File    :choose_member_method_page.py
import logging

import allure

from homework0701.po.add_member_page import AddMemberPage
from homework0701.po.basepage import BasePage


# 选择添加成员方式页
class ChooseMemberMethodPage(BasePage):

    def click_manual_input(self):
        # 点击手动输入添加
        # 进入编辑成员页
        with allure.step('点击手动输入添加'):
            self.uiauto_find('new UiSelector().text("手动输入添加")').click()
            logging.info('点击手动输入添加')
        return AddMemberPage(self.driver)

    def get_toast_text(self):
        with allure.step('获取toast:保存成功'):
            toast_text = self.get_toast('//*[@class="android.widget.Toast"]')
            logging.info(f'获取toast:{toast_text}')
        return toast_text
