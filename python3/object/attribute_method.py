#!/usr/bin/python3

"""
类属性与方法
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。

self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。

"""


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('百度', 'www.baidu.com')
x.who()  # 正常输出
x.foo()  # 正常输出
# x.__foo()  # 报错

"""
Python3 中类的静态方法、普通方法、类方法

静态方法: 用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，可以直接使用类名调用。

普通方法: 默认有个self参数，且只能被对象调用。

类方法: 默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器。
"""

class Classname:
    @staticmethod
    def fun():
        print('静态方法')

    @classmethod
    def a(cls):
        print('类方法')

    # 普通方法
    def b(self):
        print('普通方法')



Classname.fun()
Classname.a()

C = Classname()
C.fun()
C.a()
C.b()
