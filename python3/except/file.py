#!/usr/bin/python3

print("读取的文件内容：")
with open("myfile.txt", mode='r') as f:
    for line in f:
        print(line, end="")
