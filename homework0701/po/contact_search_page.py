# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 20:18
# @Author  : wkRonin
# @File    :contact_search_page.py
import logging
from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.po.basepage import BasePage


# 成员搜索页
class ContactSearchPage(BasePage):

    _search_element = (MobileBy.ID, 'com.tencent.wework:id/g5f')
    _resultlist = (MobileBy.ID, 'com.tencent.wework:id/e0p')

    def get_search_result(self, name):
        """
        获取搜索结果的数量
        :return:
        """
        with allure.step(f'输入搜索内容: {name}'):
            self.find_and_sendkeys(*self._search_element, name)
            logging.info(f'输入搜索内容: {name}')
        sleep(1)
        with allure.step('获取搜索结果列表'):
            result = self.finds(*self._resultlist)
            result_length = len(result)
            logging.info(f'获取的列表长度: {result_length}')
        return result_length
