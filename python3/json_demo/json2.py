#!/usr/bin/python3

import json

data = {"id": 100, "name": "jason", "age": "30"};

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)


# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)

print(data);