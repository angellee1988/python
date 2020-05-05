#!/usr/bin/python3

print("你好，世界")

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错
    print ("False")

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# 同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

'''
print 输出
'''
print('\n---------')
x="a"
y="b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x),
print(y)

# 不换行输出
print(x,y)