#!/usr/bin/python3

sites = ["Baidu", "Google", "Weixin", "Taobao"]
for site in sites:
    if site == "Weixin":
        print("微信!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!\n")

for i, site in enumerate(sites):
    print(i, site)

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

# 冒泡排序
print("\n冒泡排序")


def paixu(li):
    max = 0
    for ad in range(len(li) - 1):
        for x in range(len(li) - 1 - ad):
            if li[x] > li[x + 1]:
                max = li[x]
                li[x] = li[x + 1]
                li[x + 1] = max
            else:
                max = li[x + 1]
    print(li)


paixu([41, 23344, 9353, 5554, 44, 7557, 6434, 500, 2000])

# 选择排序
print("\n选择排序")

A = [64, 25, 12, 22, 11]

for i in range(len(A)):

    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print("排序后的数组：")
for i in range(len(A)):
    print(A[i], end=" "),

# 更简单的方式
print("\n调用sort方法排序")
A.sort()
print(A)
