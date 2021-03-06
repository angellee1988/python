#!/usr/bin/python3

"""
xlsxwriter 模块，它生成的文件后缀名为.xlsx，最大能够支持1048576行数据，16384列数据

"""
import xlsxwriter


# 写excel
def write_excel():
    workbook = xlsxwriter.Workbook('batch_write.xlsx')  # 创建一个excel文件
    worksheet = workbook.add_worksheet(u'sheet1')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1
    # worksheet.set_column('A:A', 20)  # 设置第一列宽度为20像素
    # bold = workbook.add_format({'bold': True})  # 设置一个加粗的格式对象
    #
    # worksheet.write('A1', 'HELLO')  # 在A1单元格写上HELLO
    # worksheet.write('A2', 'WORLD', bold)  # 在A2上写上WORLD,并且设置为加粗
    # worksheet.write('B2', U'中文测试', bold)  # 在B2上写上中文加粗

    for row in range(100000):
        for col in range(5):
            worksheet.write(row, col, row * col)

    # worksheet.write(2, 0, 32)  # 使用行列的方式写上数字32,35,5
    # worksheet.write(3, 0, 35.5)  # 使用行列的时候第一行起始为0,所以2,0代表着第三行的第一列,等价于A4
    # worksheet.write(4, 0, '=SUM(A3:A4)')  # 写上excel公式
    workbook.close()


if __name__ == '__main__':
    # 写入Excel
    write_excel();
    print('写入成功')
