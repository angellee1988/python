#!/usr/bin/python3

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))

print("\n")
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('12'.zfill(5))  # 在数字的左边填充 0

print('{0} 和 {1}'.format('Google', 'Baidu'))

print('{name}网址： {site}'.format(name='百度', site='www.baidu.com'))

import math

print('常量 PI 的值近似为： {}。'.format(math.pi))

# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化
print('常量 PI 的值近似为： {!r}。'.format(math.pi))

# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
print("\n美化表格")
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))


"""
读取键盘输入
Python提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。

input 可以接收一个Python表达式作为输入，并将运算结果返回。
"""
str = input("请输入：");
print ("你输入的内容是: ", str)