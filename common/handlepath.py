"""
============================
Author:luli
time:2020/2/23
company:happy
============================
"""

import os

# 获取当前项目的目录：父级的父级
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASEDIR)
# 用例模块的路径
CASEDIR = os.path.join(BASEDIR, 'testcases')

# 用例数据的路径
DATADIR = os.path.join(BASEDIR, 'data')

# 测试报告的路径
REPORTDIR = os.path.join(BASEDIR, 'reports')

# 配置文件的路径
CONFDIR = os.path.join(BASEDIR, 'conf')

# 日志文件的路径
LOGDIR = os.path.join(BASEDIR, 'log')
