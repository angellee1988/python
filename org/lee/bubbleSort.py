#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 冒泡排序# 定义列表 list
arays = [1,8,2,6,3,9,4,5]
for i in range(len(arays)):
    for j in range(i+1):
        if arays[i] < arays[j]:
            # 实现连个变量的互换
            arays[i],arays[j] = arays[j],arays[i]
print(arays)


a = 2
b = 3
# t = 0
a , b = b ,a
# t = a
# a = b
# b = t

print(a," ",b)


'''
100以内的质数
'''
num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)

