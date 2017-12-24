#!/usr/bin/env Python
'#!/usr/bin/python'
#coding=utf-8
'''
Created on 2017年12月23日

@author: xingjiang.li
'''

'''
Python 表达式	结果	描述
len((1, 2, 3))	3	计算元素个数
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
3 in (1, 2, 3)	True	元素是否存在
for x in (1, 2, 3): print x,	1 2 3	迭代
'''
#元组
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出第二个至第三个的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组

print(tuple[-2]) # 倒数第二个
print(tuple[-3:]) # 后3个

# tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
# list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tuple[2] = 1000    # 元组中是非法应用
# list[2] = 1000     # 列表中是合法应用

# 元组是不允许更新的