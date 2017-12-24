#!/usr/bin/env Python
'#!/usr/bin/python'
#coding=utf-8
'''
@author: xingjiang.li
'''
# str = input("请输入：");
# print("你输入的内容是: ", str)

# 打开一个文件
# fo = open("for.py", "wb")
# print("文件名: ", fo.name)
# print("是否已关闭 : ", fo.closed)
# print("访问模式 : ", fo.mode)

# 打开一个文件
# fo = open("foo.txt", "wb")
# fo.write("www.runoob.com!\nVery good site!\n");
# # 关闭打开的文件
# fo.close()

fo = open("foo.txt", "r+")
str = fo.read(10);
print("读取的字符串是 : ", str)
# 关闭打开的文件
fo.close()