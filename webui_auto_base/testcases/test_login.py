#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os.path

import pytest
import ddt,yaml,logging
from page.login_page import login
from utils.data_utils import DataUtils

from utils.GetYaml_utils import getyaml
from conftest import BASE_DIR
testData = getyaml(BASE_DIR.DATA_DIR / "test/login_data.yaml").alldata()
test_url = BASE_DIR.base_url

class TestUIAUTO:
    """登录测试"""

    def user_login_verify(self,username,password,driver,url):
        """
        用户登录
        :param user: 用户名
        :param password: 密码
        :return:
        """
        login(selenium_driver=driver,base_url=url).user_login(username,password)
    @pytest.mark.parametrize("datayaml", testData)
    def test_login(self,datayaml,setup_teardown,assert_utils):
        """
        登录测试
        :param datayaml: 加载login_data登录测试数据
        :return:
        """
        driver = setup_teardown
        url = test_url
        logging.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'],datayaml['detail']))
        # 调用登录方法
        self.user_login_verify(datayaml['data']['username'],datayaml['data']['password'],driver,url)
        po = login(driver,test_url)
        if datayaml['screenshot'] == 'user_pawd_success':
            logging.info("检查点-> {0}".format(po.user_login_success_hint()))
            assert_utils.assert_equal(po.user_login_success_hint(), datayaml['check'][0], "成功登录，返回实际结果是->: {0}".format(po.user_login_success_hint()))
            logging.info("成功登录，返回实际结果是->: {0}".format(po.user_login_success_hint()))
            driver.get_screenshot_as_file(str(BASE_DIR.REPORTS_DIR) + "/screenshot/{0}.png".format(datayaml['screenshot']))
        elif datayaml['screenshot'] == 'user_pawd_empty':
            logging.info("检查点-> {0}".format(po.user_error_hint()))
            assert_utils.assert_equal(po.user_error_hint(),datayaml['check'][0] , "异常登录，返回实际结果是->: {0}".format(po.user_error_hint()))
            logging.info("异常登录，返回实际结果是->: {0}".format(po.user_error_hint()))
            driver.get_screenshot_as_file(str(BASE_DIR.REPORTS_DIR) + "/screenshot\{0}.png".format(datayaml['screenshot']))
            driver.get_screenshot_as_file(f"{str(BASE_DIR.REPORTS_DIR)}/screenshot/{datayaml['screenshot']}.png")
        elif datayaml['screenshot'] == 'user_empty':
            logging.info("检查点-> {0}".format(po.user_error_hint()))
            assert_utils.assert_equal(po.user_error_hint(),datayaml['check'][0] , "异常登录，返回实际结果是->: {0}".format(po.user_error_hint()))
            logging.info("异常登录，返回实际结果是->: {0}".format(po.user_error_hint()))
            driver.get_screenshot_as_file(str(BASE_DIR.REPORTS_DIR) + "/screenshot\{0}.png".format(datayaml['screenshot']))
        elif datayaml['screenshot'] == 'pawd_empty':
            logging.info("检查点-> {0}".format(po.pwd_error_hint()))
            assert_utils.assert_equal(po.pwd_error_hint(),datayaml['check'][0] , "异常登录，返回实际结果是->: {0}".format(po.pwd_error_hint()))
            logging.info("异常登录，返回实际结果是->: {0}".format(po.pwd_error_hint()))
            driver.get_screenshot_as_file(str(BASE_DIR.REPORTS_DIR) + "/screenshot\{0}.png".format(datayaml['screenshot']))
        elif datayaml['screenshot'] == 'pawd_error':
            logging.info("检查点-> {0}".format(po.user_or_pwd_hint()))
            assert_utils.assert_equal(po.user_or_pwd_hint(),datayaml['check'][0] , "异常登录，返回实际结果是->: {0}".format(po.user_or_pwd_hint()))
            logging.info("异常登录，返回实际结果是->: {0}".format(po.user_or_pwd_hint()))
            driver.get_screenshot_as_file(str(BASE_DIR.REPORTS_DIR) + "/screenshot\{0}.png".format(datayaml['screenshot']))
