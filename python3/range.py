# !/usr/bin/python3

# 使用range生成数列
for i in range(5):
    print(i, end=" ")

print("\n")
for i in range(3, 8):
    print(i, end=" ")

print("\n")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
