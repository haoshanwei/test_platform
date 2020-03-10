"""
============================
Author:luli
time:2020/2/23
company:happy
============================
"""
import os
import logging
from common.handleconf import conf
from common.handlepath import LOGDIR


class HandleLog(object):
    @staticmethod
    def create_log():
        # 创建收集器，设置收集器的等级
        mylog = logging.getLogger(conf.get('log', 'name'))

        # 设置日志收集器的等级
        mylog.setLevel(conf.get('log', 'level'))

        # 创建输出到控制台的渠道，并设置等级
        sh = logging.StreamHandler()
        sh.setLevel(conf.get('log', 'sh_level'))
        mylog.addHandler(sh)

        # 设置输出到文件的渠道，并设置等级
        filepath = os.path.join(LOGDIR, 'log.log')
        fh = logging.FileHandler(filename=filepath, encoding='utf8')
        fh.setLevel(conf.get('log', 'fh_level'))
        mylog.addHandler(fh)

        # 设置日志输出格式
        fm = logging.Formatter(conf.get('log', 'format'))
        sh.setFormatter(fm)
        fh.setFormatter(fm)

        return mylog


log = HandleLog.create_log()
