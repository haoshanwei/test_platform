"""
============================
Author:luli
Time:2020/3/5
Company:Happy
============================
"""
import os
import random
import unittest
from library.ddt import ddt, data
from common.handlepath import DATADIR
from common.handlerequest import SendRequest
from common.readexcel import ReadExcel
from common.handleconf import conf
from common.handledata import replace_data
from common.handlelog import log
from common.connectdb import DB

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestMainlflow(unittest.TestCase):
    excel = ReadExcel(case_file, 'mainflow')
    datas = excel.read_data()
    request = SendRequest()
    db = DB()

    @data(*datas)
    def test_mainflow(self, case):
        # 准备测试数据
        url = conf.get('env', 'url') + replace_data(case['url'])
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        phone = self.random_phone()
        case['data'] = replace_data(case['data'])
        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()

        # 对预期结果和响应结果进行断言
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

    def random_phone(self):
        # 去数据库查询生成的手机号存不存在，不存在可以返回，存在的话需要重新生成
        random_num = ''.join(random.sample('0123456789', 8))
        phone = '130' + random_num
        sql = 'SELECT * from futureloan.member where mobile_phone = {}'.format(phone)
        if self.db.find_one(sql):
            self.random_phone()
        return phone
