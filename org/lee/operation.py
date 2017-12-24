#!/usr/bin/env Python
'#!/usr/bin/python'
#coding=utf-8
'''
Created on 2017年12月23日

@author: xingjiang.li
'''
'''
算术运算符
运算符	描述	实例
+	加 - 两个对象相加	a + b 输出结果 30
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
/	除 - x除以y	b / a 输出结果 2
%	取模 - 返回除法的余数	b % a 输出结果 0
**	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
//	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
'''

'''
比较运算符
==	等于 - 比较对象是否相等	(a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 true.
<>	不等于 - 比较两个对象是否不相等	(a <> b) 返回 true。这个运算符类似 != (python3.6不支持)。
>	大于 - 返回x是否大于y	(a > b) 返回 False。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 true。
>=	大于等于	- 返回x是否大于等于y。	(a >= b) 返回 False。
<=	小于等于 -	返回x是否小于等于y。	(a <= b) 返回 true。
'''

'''
赋值运算符
运算符	描述	实例
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
'''

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)


c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)

a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)

a = 21
b = 10
c = 0

if (a == b):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if (a != b):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

# if (a <> b):
#     print("3 - a 不等于 b")
# else:
#     print("3 - a 等于 b")

if (a < b):
    print("4 - a 小于 b")
else:
    print("4 - a 大于等于 b")

if (a > b):
    print("5 - a 大于 b")
else:
    print("5 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if (a <= b):
    print("6 - a 小于等于 b")
else:
    print
    "6 - a 大于  b"

if (b >= a):
    print("7 - b 大于等于 a")
else:
    print("7 - b 小于 a")