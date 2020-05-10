import win32com.client as win32

excel = win32.gencache.EnsureDispatch('Excel.Application')


def test_win32com_read():
    # wb = excel.Workbooks.Open('E:\\excel\\test_cases\\read_xls.xls')
    wb = excel.Workbooks.Open('E:\\excel\\test_cases\\read_xlsx.xlsx')
    # excel.Visible = True


wb = excel.Workbooks.Add()


def test_win32com_write():
    for i in range(1):
        ws = wb.Worksheets.Add()
        ws.Range("A1:ATD2000").Value = 65536

    wb.SaveAs('E:\\excel\\test_cases\\write_xlsx.xlsx')
    excel.Application.Quit()