#!/usr/bin/env Python
'#!/usr/bin/python'
#coding=utf-8
'''
Created on 2017年12月23日

@author: xingjiang.li
'''

'''
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dict1 = {}
dict1['one'] = "This is one"
dict1[2] = "This is two"

dict2 = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict1['one'])  # 输出键为'one' 的值
print(dict1[2])  # 输出键为 2 的值
print(dict2)  # 输出完整的字典
print(dict2.keys())  # 输出所有键
print(dict2.values())  # 输出所有值

#dictionary 字典相当于 java中的Map

# list = [dict,tinydict]
# print(list[0].keys())

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

del dict['Name'];  # 删除键是'Name'的条目
# dict.clear();  # 清空词典所有条目
# del dict;  # 删除词典

print("dict['Age']: ", dict['Age']);
# print("dict['School']: ", dict['School']);

'''
字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
'''
# dict = {['Name']: 'Zara', 'Age': 7};
dict = {('Name'): 'Zara', 'Age': 7}; #元组可以作为key

print("dict['Name']: ", dict['Name']);

dict_copy = dict.copy()

print(dict_copy is dict)

d={}
dict.update(d)
print(dict)
print(d)

print(dict.popitem()) #随机返回并删除字典中的一对键和值
