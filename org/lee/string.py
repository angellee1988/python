#!/usr/bin/env Python
'#!/usr/bin/python'
#coding=utf-8
'''
Created on 2017年12月23日

@author:xingjiang.li
'''

str = 'Hello World!'

print(str)  # 输出完整字符串
print(str[0])  # 输出字符串中的第一个字符
print(str[2:5])  # 输出字符串中第三个至第五个之间的字符串
print(str[2:])  # 输出从第三个字符开始的字符串
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 输出连接的字符串

print('\\')

print("r\n")
print("Bye!")

print("My name is %s and weight is %d kg!"%('Zara', 21))

str = '''
hello python!
python中三引号可以将复杂的字符串进行复制:
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）
'''

print(str)

# 引号前小写的"u"表示这里创建的是一个 Unicode 字符串
print(u'Hello\u0020World !')

print("1111111a".isdigit())

print("abcd".islower())

print("Rtyui".upper())

print("sgjkjll".title()) #返回"标题化"的 string,就是说所有单词都是以大写开始

print("Sgjkjll".istitle())
