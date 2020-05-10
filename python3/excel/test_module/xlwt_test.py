import xlwt

book = xlwt.Workbook()


def test_xlwt():
    for s in range(5):
        sheet = book.add_sheet(str(s))
        for i in range(2000):
            for j in range(256):
                sheet.write(i, j, 65536)
    book.save('test_cases\\write_xls.xls')