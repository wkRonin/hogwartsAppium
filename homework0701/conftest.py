# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 22:56
# @Author  : wkRonin
# @File    :conftest.py
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例的name和nodeid的中文显示在控制台上
    name: 用例的名称
    nodeid：用例的路径
    :param items: 收集到的所有用例
    :return:
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')