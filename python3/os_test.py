#!/usr/bin/python3

import os, glob
import re
import math
import random

print(dir(os))

print(help(os))

# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
print(glob.glob('*.py'))

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print('tea for too'.replace('too', 'two'))

print(math.cos(math.pi / 4))

print(random.random())
print(random.randrange(6))
