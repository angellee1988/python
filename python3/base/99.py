#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 九九乘法表

print("\n99乘法表")
i = 1
while i <= 9:
    # 里面一层循环控制每一行中的列数
    j = 1
    while j <= i:
        mut = j * i
        print("%d*%d=%d" % (j, i, mut), end="  ")
        j += 1
    print("")
    i += 1
