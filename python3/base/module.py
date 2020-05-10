#!/usr/bin/python3
# 文件名: using_sys.py

import sys
from python3.package import support
from python3.package import fibo

'''
__name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，
我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
'''

dir(fibo)

if __name__ == '__main__':
   print('[module]程序自身在运行')
else:
   print('[module]我来自另一模块')

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')


# 现在可以调用模块里包含的函数了
support.print_func("jason")


fibo.fib(10)