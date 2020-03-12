"""
============================
Author:luli
Time:2020/3/11
Company:Happy
============================
"""

import os
import unittest
import jsonpath
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.handlepath import DATADIR
from common.handlerequest import SendRequest
from common.handleconf import conf
from common.handlelog import log
from common.handledata import CaseData, replace_data, random_data

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class Testcases(unittest.TestCase):
    excel = ReadExcel(case_file, 'testcases')
    datas = excel.read_data()
    request = SendRequest()

    @classmethod
    def setUpClass(cls) -> None:
        url = conf.get('env', 'url') + '/user/login/'
        method = 'post'
        data = {
            'username': conf.get('test_data', 'user'),
            'password': conf.get('test_data', 'pwd')
        }
        response = cls.request.send(url=url, method=method, json=data)
        res = response.json()
        CaseData.token = 'JWT ' + jsonpath.jsonpath(res, '$.token')[0]

    @data(*datas)
    def test_cases(self, case):
        # 准备测试数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = {'Authorization': CaseData.token}
        CaseData.case_name = random_data()
        case['data'] = replace_data(case['data'])
        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        status = response.status_code

        # 对预期结果和相应结果进行断言
        try:
            self.assertEqual(expected['status'], status)
            if '成功' not in case['title']:
                self.assertIn(expected['msg'], str(res.values()))

        except AssertionError as E:
            print('预期结果：', expected)
            print('实际结果：', status, res)
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')
