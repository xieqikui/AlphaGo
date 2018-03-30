# -*- coding:utf-8 -*-
import sys
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

class SendPlainEmail():
	def __init__(self, senderaddr, senderpwd, receiveraddr, smtpserver, etext, efrom, eto, esubject, smptport):
		self.senderaddr = senderaddr
		self.senderpwd = senderpwd
		self.receiveraddr = receiveraddr
		self.smtpserver = smtpserver
		self.etext = etext
		self.efrom = efrom
		self.eto = eto
		self.esubject = esubject
		self.smptport = int(smptport)
	def __formataddr__(self, s):
		name, addr = parseaddr(s)
		print ('name:' ,name)
		print ('addr:' ,addr)
		print ('formataddr:' ,formataddr((Header(name, 'utf-8').encode(), addr)))
		return formataddr((Header(name, 'utf-8').encode(), addr))
	def __emailcontent__(self):
		msg = MIMEText(self.etext, 'plain', 'utf-8')
		msg['From'] = self.__formataddr__(self.efrom + '<' + self.senderaddr + '>') 
		msg['To'] = self.__formataddr__(self.eto + '<' + self.receiveraddr + '>')
		msg['Subject'] = Header(self.esubject, 'utf-8').encode()
		return msg
	def __smptsendemail__(self):
		msg = self.__emailcontent__()
		try:
			# server = smtplib.SMTP_SSL()
			server = smtplib.SMTP_SSL(self.smtpserver, self.smptport)
			server.set_debuglevel(1)
			# server.connect(smtpserver, 465)
			server.login(self.senderaddr, self.senderpwd)
			server.sendmail(self.senderaddr, self.receiveraddr, msg.as_string())
			print ('Send successfully')
		except Exception as e:
			print ('Send fail')
		finally:
			server.quit()
if __name__ == '__main__':
	senderaddr = '******@qq.com'
	# senderpwd = '******'
	senderpwd = '******'
	receiveraddr = '******'
	# smtpserver = 'smtp.163.com'
	smtpserver = 'smtp.qq.com'
	etext = '使用python编程语言中email模块和smtp模块实现发邮件功能！'
	efrom = 'QQ邮箱'
	eto = '163邮箱'
	esubject = '邮件发送功能测试......'
	smptport = 465
	obj = SendPlainEmail(senderaddr, senderpwd, receiveraddr, smtpserver, etext, efrom, eto, esubject, smptport)
	obj.__smptsendemail__()


