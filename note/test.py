"""
============================
Author:luli
time:2020/2/26
company:happy
============================
"""
from common.connectdb import DB
from decimal import Decimal

db = DB()

# sql = 'SELECT count(member_id) FROM futureloan.loan WHERE member_id=9591519'
# res = db.find_one(sql)['count(member_id)']
# print(res)

# sql = 'SELECT id FROM  futureloan.loan WHERE status = 2 and amount<10000;'
# loan_id = db.find_one(sql)['id']
# print(loan_id)

# sql2 = 'SELECT sum(amount) FROM  futureloan.invest WHERE loan_id=1781'
# amount = db.find_one(sql2)
#
# print(amount)

sql1 = 'SELECT amount FROM  futureloan.loan WHERE id=27;'
project_amount = db.find_one(sql1)['amount']
print(project_amount)
sql2 = 'SELECT sum(amount) FROM  futureloan.invest WHERE loan_id=27;'
invest_amount = db.find_one(sql2)['sum(amount)']
print(invest_amount)
# # 将剩余的竞标金额+100，来测试投资金额大于项目可投余额
# leave_amout = project_amount - invest_amount + Decimal('100')
# print(leave_amout)

# num = 12345
# num = num // 100 * 100
# print(num)

# sql_invest = 'SELECT count(member_id) FROM futureloan.invest WHERE member_id={} and loan_id={}'.format(8129, 13)
# start_invest_num = db.find_one(sql_invest)['count(member_id)']
# print(start_invest_num)
