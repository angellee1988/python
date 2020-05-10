#!/usr/bin/python3


# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b


n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))


var = 1
while var == 1:  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    if num == 0:
        break
    print("你输入的数字是: ", num)

print("Good bye!")