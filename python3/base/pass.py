#!/usr/bin/env Python
'#!/usr/bin/python'
#coding=utf-8
'''
Created on 2017年12月23日
@author: xingjiang.li
'''

'''
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
'''
# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print('这是 pass 块')
   print('当前字母 :', letter)

print("Good bye!")