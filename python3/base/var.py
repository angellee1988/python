#!/usr/bin/python3

"""
Python 中的变量赋值不需要类型声明。

每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。

每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值
"""
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1

print(a, b, c)

a, b, c = 1, 2, "john"
print(a, b, c)

"""
标准数据类型
Python有五个标准的数据类型：

Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）

"""



"""
Python支持四种不同的数字类型：

int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数
"""