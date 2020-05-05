#!/usr/bin/python3

from urllib.request import urlopen


response = urlopen("http://www.baidu.com/")  # 打开网站
fi = open("project.txt", 'w')  # open一个txt文件
page = fi.write(str(response.read()))  # 网站代码写入
fi.close()


# for line in urlopen('http://www.baidu.com'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     print(line)

# fi = open("project.txt", 'w')  # open一个txt文件
# page = fi.write(str(line))  # 网站代码写入
# fi.close()
