"""
============================
Author:luli
time:2020/2/23
company:happy
============================
"""
import os
import unittest
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.handlepath import DATADIR
from common.handlerequest import SendRequest
from common.handleconf import conf
from common.handlelog import log

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestLogin(unittest.TestCase):
    excel = ReadExcel(case_file, 'login')
    datas = excel.read_data()
    request = SendRequest()

    @data(*datas)
    def test_login(self, case):
        # 准备测试数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        # 对预期结果和相应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except AssertionError as E:
            print('预期结果：', expected)
            print('实际结果：', res)
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')
            log.info("用例：{}，执行未通过".format(case['title']))
