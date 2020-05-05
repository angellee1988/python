#!/usr/bin/python3

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 删除重复的

# 集合操作
a = set('abracadabra')
b = set('alacazam')
print(a)  # a 中唯一的字母
print(a - b)  # 在 a 中的字母，但不在 b 中
print(a | b)  # 在 a 或 b 中的字母
print(a & b)  # 在 a 和 b 中都有的字母
print(a ^ b)  # 在 a 或 b 中的字母，但不同时在 a 和 b 中

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

var = {x: x ** 2 for x in (2, 4, 6)}
print(var)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print("k=", k, ",v=", v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 列表推导式
vec = [2, 4, 6]

v = [3 * x for x in vec]
print(v)
vv = [[x, x ** 2] for x in vec]
print(vv)


u = [3*x for x in vec if x > 3]
print(u)

# 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

m = [[row[i] for row in matrix] for i in range(4)]
print(m)
