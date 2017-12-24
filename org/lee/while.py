#!/usr/bin/env Python
'#!/usr/bin/python'
#coding=utf-8

'''
Created on 2017年12月23日
@author: xingjiang.li
'''

count = 0
while (count < 9):
    count = count + 1
    if count % 2 == 1 :
        continue
    print('The count is:', count)
print("Good bye!")

'''
while … else 在循环条件为 false 时执行 else 语句块
'''
count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")

'''
类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中
'''
flag = 1

while (flag): print('Given flag is really true!')

print("Good bye!")