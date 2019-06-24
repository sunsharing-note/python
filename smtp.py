# coding=utf-8
import smtplib
from email.mime.text import MIMEText
#设置服务器所需信息
mail_host='smtp.126.com'
mail_user='cxf210210@126.com'
mail_pass='asdASD123'
sender='cxf210210@126.com'
receivers=['cxf210210@163.com','wahaha5354@qq.com']
#设置email信息
#邮件内容设置
message=MIMEText('python send mail success','plain','utf-8')
#邮件主题
message['Subject']='title'
#发送方信息
message['From']=sender
#接收方信息
message['To']=receivers[1]

#登录并发送邮件
try:
	smtpOBj=smtplib.SMTP()
	#连接到服务器
	smtpOBj.connect(mail_host,25)
	#登录到服务器
	smtpOBj.starttls()
	smtpOBj.login(mail_user,mail_pass)
	#发送
	smtpOBj.sendmail(sender,receivers,message.as_string())
	#退出
	smtpOBj.quit()
	print('success')
except smtplib.SMTPException as e:
	print('error',e)
