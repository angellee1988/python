#!/usr/bin/env Python
'#!/usr/bin/python'
#coding=utf-8

'''
Created on 2017年12月23日
@author: xingjiang.li
'''
num = 5
if num == 3:            # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:           # 值小于零时输出
    print('error')
else:
    print('roadman')     # 条件均不成立时输出

'''
由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，
如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；
使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
'''

num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print('hello')
# 输出结果: hello

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print('hello')
else:
    print('undefine')
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')
else:
    print('undefine')

var = 100

if (var == 100): print("变量 var 的值为100")

print("Good bye!")

'''
python 复合布尔表达式计算采用短路规则，即如果通过前面的部分已经计算出整个表达式的值，
则后面的部分不再计算
'''
a=0
b=1
if ( a > 0 ) and ( b / a > 2 ):
    print("yes")
else :
    print("no")