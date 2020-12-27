#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "xxx@xx.com"  # 用户名
mail_pass = "xxxx"  # 口令

sender = 'xxx@xx.com'
receivers = ['xxx@xx.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("Jason", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test1.txt 文件
att1 = MIMEText(open('test1.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test1.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的 test2.txt 文件
att2 = MIMEText(open('test2.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="test2.txt"'
message.attach(att2)

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    # smtpObj = smtplib.SMTP()
    # smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件", e)
