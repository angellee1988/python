#!/usr/bin/python3

"""
类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，
类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
"""


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('jason', 10, 30)
p.speak()

"""
继承
Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:

class DerivedClassName(BaseClassName1):
    <statement-1>
    .
    .
    .
    <statement-N>
BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:

class DerivedClassName(modname.BaseClassName):
"""


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()

"""
多继承
Python同样有限的支持多继承形式。多继承的类定义形如下例:

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
"""


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法

print("\n-----方法重写-----")


# 方法重写
class Parent:  # 定义父类
    def __init__(self):
        print("初始化父类构造")

    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def __init__(self):  # 有了子类的构造方法，就不去调用父类的构造了
        print("初始化子类构造")

    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法

