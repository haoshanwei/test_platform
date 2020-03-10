"""
============================
Author:luli
Time:2020/3/3
Company:Happy
============================
"""
import os
import unittest
import jsonpath
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.handlepath import DATADIR
from common.handleconf import conf
from common.handlelog import log
from common.handlerequest import SendRequest
from common.connectdb import DB
from common.handledata import CaseData, replace_data

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestUpdate(unittest.TestCase):
    excel = ReadExcel(case_file, 'update')
    datas = excel.read_data()
    request = SendRequest()
    db = DB()

    @data(*datas)
    def test_update(self, case):
        # 准备数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = getattr(CaseData, 'token_value')
        # 替换数据
        case['data'] = replace_data(case['data'])
        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1

        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        # 获取用户ID
        if case['title'] == '登录':
            CaseData.member_id = str(jsonpath.jsonpath(res, '$..id')[0])
            CaseData.token_value = jsonpath.jsonpath(res, '$..token_type')[0] + ' ' + \
                                   jsonpath.jsonpath(res, '$..token')[0]
        # 对预期结果和响应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            # 对更新成功的用例进行数据库校验
            if case['check_sql']:
                sql = replace_data(case['check_sql'])
                reg_name = self.db.find_one(sql)['reg_name']
                self.assertEqual(data['reg_name'], reg_name)

        except AssertionError as E:
            print('预期结果：', expected['msg'])
            print('实际结果：', res['msg'])
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')
