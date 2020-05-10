#!/usr/bin/env Python
'#!/usr/bin/python'
# coding=utf-8
'''
@author: xingjiang.li
'''

'''
Python内置类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
'''

'''
self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
'''


class User:
    '用户信息'
    userName = ''
    password = ''
    age = 0

    # __init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def __init__(self, userName, password, age):
        self.userName = userName
        self.password = password
        self.age = age

    '打印用户信息'

    def showUser(self):
        print("userName:", self.userName)
        print("age:", self.age)

    # 析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")


user = User('小明', '123456', 23)
user.showUser()

print(User.__dict__)
print(User.__doc__)

'''
python对象销毁(垃圾回收)
Python 使用了引用计数这一简单技术来跟踪和回收垃圾。
在 Python 内部记录着所有使用中的对象各有多少引用。
一个内部跟踪变量，称为一个引用计数器。
当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时，
也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。
但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。
'''

'''
垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。
循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。
这种情况下，仅使用引用计数是不够的。
Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。
作为引用计数的补充， 垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。
 在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。
'''
