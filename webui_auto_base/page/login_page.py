#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : 北京-瑛智
from selenium.webdriver.common.by import By
from page.base_page import Page
from time import sleep
from conftest import BASE_DIR
from utils.GetYaml_utils import getyaml
testData = getyaml(BASE_DIR.DATA_DIR / "test/login.yaml")


class login(Page):
    """
    用户登录页面
    """
    # 定位器，通过元素属性定位元素对象
    # 手机号输入框
    login_user_loc = (testData.get_find_type(0),testData.get_elementinfo(0))

    # 密码输入框
    login_password_loc = (testData.get_find_type(1),testData.get_elementinfo(1))

    # 取消自动登录
    keeplogin_button_loc = (testData.get_find_type(2),testData.get_elementinfo(2))

    # 单击登录
    login_button_loc = (testData.get_find_type(3),testData.get_elementinfo(3))


    def login_user(self,user):
        """
        登录手机号
        :param username:
        :return:
        """
        self.find_element(*self.login_user_loc).send_keys(user)

    def login_password(self,password):
        """
        登录密码
        :param password:
        :return:
        """
        self.find_element(*self.login_password_loc).send_keys(password)

    def keeplogin(self):
        """
        取消单选自动登录
        :return:
        """
        self.find_element(*self.keeplogin_button_loc).click()

    def login_button(self):
        """
        登录按钮
        :return:
        """
        self.find_element(*self.login_button_loc).click()

    # def login_exit(self):
    #     """
    #     退出系统
    #     :return:
    #     """
    #     above = self.find_element(*self.login_exit_loc)
    #     ActionChains(self.driver).move_to_element(above).perform()
    #     sleep(2)
    #     self.find_element(*self.login_exit_button_loc).click()

    def user_login(self,username,password):
        """
        登录流程
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.open()
        # self.dig_login()
        self.login_user(username)
        self.login_password(password)
        sleep(1)
        self.keeplogin()
        sleep(1)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (testData.get_CheckFindType(0),testData.get_CheckElementinfo(0))
    pwd_error_hint_loc = (testData.get_CheckFindType(1), testData.get_CheckElementinfo(1))
    user_or_pwd_error_loc = (testData.get_CheckFindType(2),testData.get_CheckElementinfo(2))
    user_login_success_loc = (testData.get_CheckFindType(3),testData.get_CheckElementinfo(3))

    #  用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text
    # 密码错误提示
    def pwd_error_hint(self):
        return self.find_element(*self.pwd_error_hint_loc).text
    # 用户名密码错误提醒
    def user_or_pwd_hint(self):
        return self.find_element(*self.user_or_pwd_error_loc).text
    # 登录成功用户名
    def user_login_success_hint(self):
        return self.switch_url()



