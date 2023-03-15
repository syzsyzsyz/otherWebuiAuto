#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz

import logging
import pytest_check as check
import re,jsonpath,jsonschema
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class AssertUtils:
	def __init__(self,capsys=None,caplog=None,driver=None,timeout=5):
		self.capsys = capsys
		self.caplog = caplog
		self.driver = driver
		self.timeout = timeout
	#webui常用断言
	def assert_title_contains(self,excepted_txt,timeout=5):
		logging.debug("断言 网页标题包含%s"%(excepted_txt))
		try:
			WebDriverWait(self.driver,timeout).until(EC.title_contains(excepted_txt))
		except TimeoutException as err:
			check.is_none(err)
	def assert_url_contains(self,excepted_txt,timeout=5):
		logging.debug("断言 网页url包含%s"%(excepted_txt))
		try:
			WebDriverWait(self.driver,timeout).until(EC.url_contains(excepted_txt))
		except TimeoutException as err:
			check.is_none(err)
	def assert_element_exist(self,by,value,timeout):
		logging.debug("断言 存在元素%s=%s"%(by,value))
		try:
			WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((by,value)))
		except TimeoutException as err:
			check.is_none(err)
	#正则 json断言
	def assert_re_match(self,actual,patten):
		logging.debug("断言 %s 匹配正则表达式%s"%(patten,actual))
		check.is_not_none(re.match(patten,actual))

	def assert_jsonpath_result_contains(self,data:dict,jsonpath_str,exceped):
		logging.debug("断言 %s 使用jsonpath %s 提取结果包含 %s"%(data,jsonpath_str,exceped))
		actual = jsonpath.jsonpath(data,jsonpath_str)
		check.is_in(exceped,actual)
	def assert_jsonschema_validate(self,data:dict,schema:dict):
		logging.debug("断言 %s符合jsonschema %s"%(data,schema))
		try:
			jsonschema.validate(data,schema)
		except jsonschema.exceptions.ValidationError as err:
			check.is_none(err)
	#异常断言
	def assert_sysout_contaions(self,excepted_txt):
		logging.debug("断言 系统包含 %s"%excepted_txt)
		sysout,syserr = self.capsys.readouterr()
		check.is_in(excepted_txt,sysout)
	def assert_log_contains(self,excepted_txt,level=logging.INFO):
		logging.debug("断言 日志输出包含 %s"%excepted_txt)
		log_msgs = []
		for logger_name,logger_level,message in self.caplog.record_tuples:
			if logger_level == level:
				log_msgs.append(message)
		check.is_in(excepted_txt,'\n'.join(log_msgs))
	def assert_raises(self,excepted_exception):
		logging.debug("断言 抛出异常 %s"%excepted_exception)
		return check.raises(excepted_exception)
	#普通断言
	def assert_equal(self, actual, excepted,str):
		logging.debug('断言 %s 等于 %s' % (actual, excepted))
		check.equal(actual, excepted,str)
	def assert_not_equal(self, actual, excepted):
		logging.debug('断言 %s 不等于 %s' % (actual, excepted))
		check.not_equal(actual, excepted)

	def assert_length_is(self, actual, number):
		logging.debug('断言 %s ËÈÊÁ %s' % (actual, number))
		check.equal(len(actual), number)

	def assert_is_true(self, actual):
		logging.debug('断言 %s 为 True' % actual)
		check.is_true(actual)

	def assert_is_false(self, actual):
		logging.debug('断言 %s 为 False' % actual)
		check.is_false(actual)

	def assert_is_none(self, actual):
		logging.debug('断言 %s 为 None' % actual)
		check.is_none(actual)

	def assert_is_not_none(self, actual):
		logging.debug('断言 %s 不为 None' % actual)
		check.is_not_none(actual)

	def assert_contains(self, actual, excepted):
		logging.debug('断言 %s 包含 %s' % actual, excepted)
		check.is_in(excepted, actual)

	def assert_in(self, actual, excepted):
		logging.debug('断言 %s 在 %s 中' % actual, excepted)
		check.is_in(actual in excepted)