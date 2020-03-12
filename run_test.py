"""
============================
Author:luli
Time:2020/3/10
Company:Happy
============================
"""
import os
import unittest
from BeautifulReport import BeautifulReport
from common.handlepath import CASEDIR, REPORTDIR
from common.handle_email import send_email

# 创建测试套件
suite = unittest.TestSuite()

# 将测试用例加载到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR))

br = BeautifulReport(suite)
br.report("前程贷项目用例", filename="report.html", report_dir=REPORTDIR)

report_file = os.path.join(REPORTDIR, 'report.html')
send_email(report_file, '接口测试报告')
