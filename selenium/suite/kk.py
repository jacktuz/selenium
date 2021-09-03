import xlrd
from xlutils.copy import copy
import os



def kkk():
    rb = xlrd.open_workbook(os.path.join(os.getcwd(), "../data/case.xlsx"))
    table1 = rb.sheets()[0]
    a1 = table1.cell(1,1).value
    a2 = table1.cell(1,2).value

    rb = xlrd.open_workbook(os.path.join(os.getcwd(), "../data/case.xlsx"))
    wb = copy(rb)
    table = wb.get_sheet(0)
    if a1 != a2:
        twd = a1
        a1 = a2
        a2 = twd

    table.write(1,1,a1)
    table.write(1,2,a2)
    wb.save('../data/case.xlsx')

if __name__ == '__main__':
    kkk()
