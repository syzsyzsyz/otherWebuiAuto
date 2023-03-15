import logging
import os.path

import pytest
import sys
def test_01(assert_utils):
	assert_utils.assert_equal(1,1)
def test_raise(assert_utils,capsys,caplog):
	assert_utils.capsys = capsys
	assert_utils.caplog = caplog
	#断言控制台输出内容
	print("hello,word")
	assert_utils.assert_sysout_contaions("hello")
	#断言输出日志柏包含
	logging.info("info message")
	assert_utils.assert_log_contains('message',logging.INFO)
	#断言抛出异常
	data = {"a":1,"b":2}
	with assert_utils.assert_raises(KeyError):
		print(data["c"])
	#断言异常信息包含
	with assert_utils.assert_raises(Exception) as err_msg:
		int("123.45")
		assert_utils.assert_in("invalid literal for int",err_msg)
def test_re_json(assert_utils):
	try:
		assert_utils.assert_re_match("value: 12",r"value: \d+")
	except:
		logging.debug("断言失败")

	assert_utils.assert_jsonpath_result_contains({'code': 0, 'data': [{'name': '张三'}]},
												 '$.data[0].name', '张三')
	assert_utils.assert_jsonschema_validate({'code': 0, 'data': [{'name': '张三'}]},
											{'type': 'object',
											 'properties': {'code': {'type': 'integer'},
															'data': {'type': 'array'}}})
# def test_data(data_dir,data_utils):
#     assert data_utils(data_dir /"test/data.",encoding="utf-8",type="json",split="-")
# def test_db(db):
#     db.query("SELECT count(*) FROM stu")
if __name__ == "__main__":
    pytest.main('-vs')