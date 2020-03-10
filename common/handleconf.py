"""
============================
Author:luli
time:2020/2/23
company:happy
============================
"""
import os
from configparser import RawConfigParser
from common.handlepath import CONFDIR


class HandleConf(RawConfigParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.read(filename, encoding='utf8')

    def write_data(self, session, key, value):
        self.set(session, key, value)
        self.write(fp=open(self.filename, 'wb'))


conf = HandleConf(os.path.join(CONFDIR, "config.ini"))

'''
RawConfigParser 与 ConfigParser
一般情况都是使用ConfigParser这个方法，但是当我们配置中有%(filename)s这种格式的配置的时候，可能会出现以下问题：
option 'xxx' in section 'xxx' contains an interpolation key ‘asctime‘ which is not a valid option name
这个时候使用RawConfigParser可以解决
'''
