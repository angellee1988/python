class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value:', e.value)

"""
以下例子不管 try 子句里面有没有发生异常，finally 子句都会执行。

如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，
而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后被抛出。
"""
try:
    raise KeyboardInterrupt
except KeyboardInterrupt as e:
    print('KeyboardInterrupt occurred')
finally:
    print('Goodbye, world!')


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)

divide(2, 0)

