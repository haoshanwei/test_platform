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


def random_data():
    user = ''.join(random.sample('0123456789zbcdefghijklmnopqrstuvwxyz', 6))
    email = user + '@163.com'
    return user, email


user, email = random_data()

request = SendRequest()
url = r'http://api.keyou.site:8000/user/register/'
method = 'post'
data = {
    "username": user,
    "email": email,
    "password": "lemon",
    "password_confirm": "lemonban"
}

# 获取结果
response = request.send(url=url, method=method, json=data)
print(response)
res = response.json()
print(list(res.values())[0])

status = response.status_code
print(status)
