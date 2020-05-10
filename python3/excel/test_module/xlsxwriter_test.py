import xlsxwriter

workbook = xlsxwriter.Workbook('test_cases\\write_xlsx.xlsx')


def test_xlsxwriter():
    for s in range(1):
        worksheet = workbook.add_worksheet()
        for i in range(2000):
            for j in range(1200):
                worksheet.write(i, j, 65536)
    workbook.close()