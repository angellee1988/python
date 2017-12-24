#!/usr/bin/env Python
'#!/usr/bin/python'
#coding=utf-8

'''
Created on 2017年12月23日
@author: xingjiang.li
'''
import random

print(random._pi)

# print(pi)

def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print(str)
   return


printme('hello')


'''
关键字参数
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
'''


'''
缺省参数
调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：
'''


# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("Name: ", name);
    print("Age ", age);
    return;

# 调用printinfo函数
printinfo(age=50, name="miki");
printinfo(name="miki",age=50);
printinfo(name="miki");

'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
加了星号（*）的变量名会存放所有未命名的变量参数
'''


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);

'''
匿名函数
python 使用 lambda 来创建匿名函数。
lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
lambda函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
'''
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))