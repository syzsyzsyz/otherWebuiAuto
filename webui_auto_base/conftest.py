#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz
import os

import pytest
from datetime import datetime
from utils.sendemail_utils import send_email
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
ChromeService = ChromeService(executable_path=ChromeDriverManager().install())
# from utils.db_utils import MySQL
import sys


from utils.db_utils import MySQL
from utils.assert_utils import AssertUtils
from selenium import webdriver
from pathlib import Path

class BASE_DIR():
	PROJRCT_DIR = Path(__file__).parent
	DATA_DIR = PROJRCT_DIR / "data"
	LOGS_DIR = PROJRCT_DIR / "logs"
	REPORTS_DIR = PROJRCT_DIR / "reports"
	ALLURE_DATA_DIR = REPORTS_DIR / "allure-data"
	ALLURE_REPORT_DIR = REPORTS_DIR / "allure-html"
	base_url = "http://115.28.108.130/newecshop/user.php"

@pytest.fixture(scope="session")
def setup_teardown():
	driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
	driver.maximize_window()
	driver.implicitly_wait(10)
	yield driver
	driver.close()
@pytest.fixture()
def assert_utils():
	return AssertUtils()

NOW = datetime.now()
def pytest_addoption(parser):
	#添加ini配置项
	parser.addini('send_email', help='auto send email or not')
	parser.addini('gen_report', help="allure generate html or not")

def pytest_configure(config):
	"""Pytest =>初始化钩子函数"""
	# 获取 pytest.ini 配置文件中的 log_file 配置项
	log_file = config.getini('log_file')
	if log_file:# 如果存在该配置项
		# 修改命令行选项中log_file参数为日志绝对路径
		config.option.log_file = config.rootdir / NOW.strftime(log_file)
	if config.getini("gen_report"):
		config.option.allure_report_dir = BASE_DIR.ALLURE_DATA_DIR
def pytest_terminal_summary(terminalreporter,exitstatus,config):

	if config.getini("gen_report"):
		gen_report_cmd = (f'allure generate {BASE_DIR.ALLURE_DATA_DIR} '
						  f'-o {BASE_DIR.ALLURE_REPORT_DIR} --clean')
		os.system(gen_report_cmd)
	# if config.getini("send_email"):
	# 	send_email()
