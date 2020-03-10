"""
============================
Author:luli
time:2020/2/23
company:happy
============================
"""
import openpyxl


class ReadExcel(object):
    def __init__(self, filename, sheet_name):
        self.filename = filename
        self.sheet_name = sheet_name

    def open(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        self.open()
        excel_data = list(self.sh.rows)
        title = [i.value for i in excel_data[0]]
        cases = []
        for i in excel_data[1:]:
            values = [j.value for j in i]
            case = dict(zip(title, values))
            cases.append(case)
        return cases

    def write_data(self, row, column, value):
        self.open()
        self.sh.cell(row=row, column=column, value=value)
        self.wb.save(self.filename)
