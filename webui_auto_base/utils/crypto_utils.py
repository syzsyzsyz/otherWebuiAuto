#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : 北京-瑛智
import logging
import base64
import hashlib

class Crypto:
	def md5(self,text:str):
		logging.debug("MD5 加密 %s"%text)
		return hashlib.md5(text.encode()).hexdigest()
	def sha256(self,text:str):
		logging.debug("生成SHA256摘要 %s" % text)
		return hashlib.sha256(text.encode()).hexdigest()
	def b64_encode(self,text:str):
		logging.debug("BASE64 编码 %s" % text)
		return base64.b64encode(text.encode()).decode()
	def b64_decode(self,base64_txt:str):
		logging.debug("BASE64 解码 %s" % base64_txt)
		return base64.b64decode(base64_txt.encode()).decode()