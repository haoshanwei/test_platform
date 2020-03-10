"""
============================
Author:luli
Time:2020/3/10
Company:Happy
============================
"""
import os
import unittest
from common.handlepath import CASEDIR, REPORTDIR
from common.handle_email import send_email
from library.HTMLTestRunnerNew import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()

# 将测试用例加载到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR, pattern='test01_register.py'))
# 创建测试运行程序
report_file = os.path.join(REPORTDIR, 'report.html')
runner = HTMLTestRunner(stream=open(report_file, 'wb'),
                        title='平台接口测试报告',
                        description='这是一份关于测试开发平台的接口测试报告',
                        tester='鹿梨')
# 执行测试运行程序
runner.run(suite)

# send_email(report_file,'前程贷最终测试报告')
