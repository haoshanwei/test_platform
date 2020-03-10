"""
============================
Author:luli
Time:2020/3/10
Company:Happy
============================
"""
import os
import unittest
import random
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.handlepath import DATADIR
from common.handlerequest import SendRequest
from common.handleconf import conf
from common.handlelog import log

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestRegister(unittest.TestCase):
    excel = ReadExcel(case_file, 'register')
    datas = excel.read_data()
    request = SendRequest()

    @data(*datas)
    def test_regiter(self, case):
        # 准备测试数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        phone = self.random_phone()
        case['data'] = case['data'].replace('#phone#', phone)
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
            if case['check_sql']:
                sql = 'SELECT id FROM futureloan.member WHERE mobile_phone={}'.format(
                    phone)
                # 查询当前用户的id
                member_id = self.db.find_one(sql)['id']
                self.assertEqual(res['data']['id'], member_id)
        except AssertionError as E:
            print('预期结果：', expected)
            print('实际结果：', res)
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')

    def random_user(self):
        user = ''.join(random.sample('0123456789zbcdefghijklmnopqrstuvwxyz', 6))
        url = r'http://api.keyou.site:8000/user/{}/count/'.format(user)
        method = 'get'
        response = self.request.get(url=url, method=method)
        res = response.json()
        if res['count'] == 1:
            self.random_user()
        return user

    def random_email(self):
        email = self.user + '163.com'
        url = r'http://api.keyou.site:8000/user/{}/count/'.format(email)
        method = 'get'
        response = self.request.get(url=url, method=method)
        res = response.json()
        if res['count'] == 1:
            self.random_user()
            self.random_email()
        return email
