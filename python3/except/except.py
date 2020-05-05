#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Python3 错误和异常
作为 Python 初学者，在刚学习 Python 编程时，经常会看到一些报错信息，在前面我们没有提及，这章节我们会专门介绍。

Python 有两种错误很容易辨认：语法错误和异常。

Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。

语法错误
Python 的语法错误或者称之为解析错，是初学者经常碰到的，如下实例

>>>while True print('Hello world')
  File "<stdin>", line 1, in ?
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
这个例子中，函数 print() 被检查到有错误，是它前面缺少了一个冒号 : 。

语法分析器指出了出错的一行，并且在最先找到的错误的位置标记了一个小小的箭头。

异常
即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。

"""

# try:
#     x = int(input("请输入一个数字: "))
# except ValueError:
#     print("您输入的不是数字，请再次尝试输入！")

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

"""
预定义的清理行为
一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。

这面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上:

for line in open("myfile.txt"):
    print(line, end="")
以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。

关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
"""

print("\n读取的文件内容：(使用utf-8编码)")
with open("myfile.txt", mode='r', encoding='UTF-8') as f:
    for line in f:
        print(line, end="")
