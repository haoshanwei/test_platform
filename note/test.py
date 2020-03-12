"""
============================
Author:luli
Time:2020/3/10
Company:Happy
============================
"""

import random
import unittest
from common.handlerequest import SendRequest
from common.handledata import CaseData


def random_data():
    user = ''.join(random.sample('0123456789zbcdefghijklmnopqrstuvwxyz', 6))
    email = user + '@163.com'
    return user, email


user, email = random_data()

request = SendRequest()
url = r'http://api.keyou.site:8000/testcases/'
method = 'post'
headers = {
    'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjE5LCJ1c2VybmFtZSI6Imx1bGk1MjAiLCJleHAiOjE1ODM5OTk2MTMsImVtYWlsIjoibmV2ZXJtb3JlQDE2My5jb20ifQ.8LOfDxe9alzZVp7PbxFeW_As8rRDBUnb-AcwkXs7fec'}
data = {
    "name": "xxxas用例",
    "interface": {
        "pid": 0,
        "iid": 1
    },
    "include": "[1,2]",
    "author": "可优",
    "request": "xxx请求数据"
}

# 获取结果
response = request.send(url=url, method=method, headers=headers, json=data)
print(response)
res = response.json()
print(str(res.values()))

respect = {'status': 400, 'msg': '所选项目不存在'}
print(respect['msg'])

