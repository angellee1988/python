#!/usr/bin/env Python
'#!/usr/bin/python'
#coding=utf-8
'''
Created on 2017年12月23日

@author: xingjiang.li
'''

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = ['123', 'john']

print(list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表


#列表是有序的，允许更新的

print(max(tinylist))

print(min(tinylist))

print(tinylist.append('Lucy'))
tinylist.append('123')
print(tinylist)
print(tinylist.count('123'))

tinylist.reverse()
print(tinylist)