#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz


import yagmail
def send_email():
	accept_user = [
		'3580****14@qq.com',
	]
	body = "Hi,all,\n附件中是测试报告，如有疑问请指出" + "\n<h2>测试报告</h2><p>以下为测试报告内容<p>"
	attachments = ["c://",
				   "D://",
				   ]
	cc_user = [
		"@.com"
	]
	bcc_user = []

	yag = yagmail.SMTP(user='3079****95@qq.com', password='nm************hd', host='smtp.qq.com')

	yag.send(to=accept_user, subject='测试报告',
			 contents=body, attachments=attachments, cc=cc_user,
			 bcc=bcc_user, preview_only=False, prettify_html=False)
