# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 18:37
# @Author  : wkRonin
# @File    :run.py
import logging
import os
import shutil

import pytest

if __name__ == '__main__':
    if os.path.exists('report/'):
        shutil.rmtree(path='report/')
    pytest.main(
        args=[
            './test_delete_member.py',
            '-vs']
            )
    logging.info('自动以服务形式打开报告')

    os.system('allure serve ./report')
