"""
============================
Author:luli
time:2020/2/23
company:happy
============================
"""

import requests


class SendRequest(object):
    def __init__(self):
        self.session = requests.session()

    def send(self, url, method, headers=None, params=None, data=None, json=None, files=None):
        method = method.lower()
        if method == 'get':
            response = self.session.get(url=url, params=params, headers=headers)
        elif method == 'post':
            response = self.session.post(url=url, headers=headers, data=data, json=json, files=files)
        elif method == 'patch':
            response = self.session.patch(url=url, headers=headers, data=data, json=json, files=files)
        else:
            print('暂不支持此方法')
        return response
