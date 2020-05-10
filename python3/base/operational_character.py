# !/usr/bin/python3

"""
Python语言支持以下类型的运算符:

算术运算符
比较（关系）运算符
赋值运算符
逻辑运算符
位运算符
成员运算符
身份运算符
运算符优先级


算术运算符
运算符	描述	实例
+	加 - 两个对象相加	a + b 输出结果 30
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
/	除 - x除以y	b / a 输出结果 2
%	取模 - 返回除法的余数	b % a 输出结果 0
**	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
//	取整除 - 返回商的整数部分（向下取整）	>>> 9//2  4     >>> -9//2  -5
"""

print("\n============算术运算符===========")
a = 21
b = 10
c = 0
d = 2

print(a + b)

print(a - b)

print(a * b)

print(a / b)

print(a // b)

print(a % b)

print(b ** d)

"""
Python比较运算符

运算符	描述	实例
==	等于 - 比较对象是否相等	(a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 true.
<>	不等于 - 比较两个对象是否不相等。python3 已废弃。	(a <> b) 返回 true。这个运算符类似 != 。
>	大于 - 返回x是否大于y	(a > b) 返回 False。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。	(a < b) 返回 true。
>=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
<=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 true。
"""
print("\n============比较运算符===========")
if a == b:
    print("a == b")
else:
    print("a != b")

if a != b:
    print("a != b")
else:
    print("a == b")

if a > b:
    print("a > b")
else:
    print("a <= b")


"""
Python赋值运算符

"""
print("\n============赋值运算符===========")
c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)


"""
Python位运算符
"""
print("\n============位运算符===========")
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b;  # 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b;  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a;  # -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2;  # 240 = 1111 0000
print("5 - c 的值为：", c)

c = a >> 2;  # 15 = 0000 1111
print("6 - c 的值为：", c)


"""
Python逻辑运算符
and 
or 
not
"""

print("\n============逻辑运算符===========")
a = 10
b = 20

if a and b:
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if a and b:
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")


"""
成员运算符
包括字符串，列表或元组

in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
"""
print("\n============成员运算符===========")
a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (b not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if (a in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")


"""
身份运算符
身份运算符用于比较两个对象的存储单元

运算符	描述	实例
is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
注： id() 函数用于获取对象内存地址。
"""
print("\n============身份运算符===========")
a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (a is not b):
    print("2 - a 和 b 没有相同的标识")
else:
    print("2 - a 和 b 有相同的标识")

# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")