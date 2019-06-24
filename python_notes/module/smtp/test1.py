#! /usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
import smtplib

msg_from = "18315293270@139.com"
msg_to = "286991486@qq.com"
passwd = "xxxxxxxxxxxxxxxxx"

subject = "python邮件测试"
content = "hello,this is my first email"
msg = MIMEText(content)
msg["Subject"] = subject
msg["From"] = msg_from
msg["To"] = msg_to

s = smtplib.SMTP_SSL("smtp.139.com",465)
s.login(msg_from,passwd)
s.sendmail(msg_from,msg_to,msg.as_string())
