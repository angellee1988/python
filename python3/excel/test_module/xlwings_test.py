import xlwings


def test_xlwings_read():
    # f = xlwings.Book('test_cases\\read_xls.xls')
    f = xlwings.Book('test_cases\\read_xlsx.xlsx')


import numpy as np

f = xlwings.Book('')
d = np.zeros([2000, 1200])
d += 65536


def test_xlwings_write():
    for s in range(1):
        sheet = f.sheets.add()
        sheet.range('A1').value = d
    f.save('test_cases\\write_xlsx.xlsx')