#!/usr/bin/python3

def hello():
    print("Hello Python3!")


hello()


# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("jason")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


def printme(str):
    print(str)


printme("哈哈哈\n")


def printlist(list):
    for d in list:
        print(d)


list = ["weixin", "qq", "baidu", "google"]
printlist(list)

"""
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""


# 不可变对象
def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)  # 结果是 2


# 传可变对象
# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)

"""
关键字参数
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
"""


# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用printme函数
printme(str="jason")


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="jason")

"""
默认参数
调用函数时，如果没有传递参数，则会使用默认参数。
"""


# 可写函数说明
def printinfo(name, age=32):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="jason")
print("------------------------")
printinfo(name="jason")

"""
 不定长参数
 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
"""


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)


# 加了两个星号 ** 的参数会以字典的形式导入
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


printinfo(1, a=2, b=3)


# 声明函数时，参数中星号 * 可以单独出现，如果单独出现星号 * 后的参数必须用关键字传入
def f(a, b, *, c):
    return a + b + c


# f(1,2,3) 错误
print(f(1, 2, c=3))  # 正确

'''
匿名函数
python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

lambda 函数的语法只包含一个语句，如下：

lambda [arg1 [,arg2,.....argn]]:expression

'''

print("\n匿名函数lambda")
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

'''
return语句
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
'''


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和.
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)
