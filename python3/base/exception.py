#!/usr/bin/python3
# coding=utf-8

try:
    fh = open("testfile.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
    1 / 0
except IOError:
    print("Error: 没有找到文件或读取文件失败")
except ZeroDivisionError as zde:
    print(zde, "Error: 除数为0")
except BaseException:
    print("Error: 程序出错")
else:
    print("内容写入文件成功")
    fh.close()

print("================================================")


# 定义函数
def mye(level):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行


try:
    mye(0)  # 触发异常
except Exception as e:
    print(e)
else:
    print(2)
finally:
    print("这里总会执行")
