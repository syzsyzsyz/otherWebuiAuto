#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz

import logging
import pymysql


#连接数据库
class MySQL:
	def __init__(self,host,user,password,db,port=3306,charset="utf8"):
		logging.debug("链接数据库->%s"%host)
		self.conn = pymysql.connect(host=host,user=user,password=password,
									port=port,
									db=db,
									charset=charset,
									autocommit=True
									)
		#创建游标对象（查询数据返回为字典格式）
		self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
	def query(self,sql):
		'''执行sql，并且返回查询结果List(Dict)'''
		self.cur.execute(sql)
		result = self.cur.fetchall()
		logging.info("查询sql->%s结果->%s"%(sql,result))
		return result
	def execute(self,sql):
		'''执行sql并返回影响行数'''
		try:
			result = self.cur.execute(sql)
			self.conn.commit()
		except Exception as msg:
			logging.exception(msg)
			self.conn.rollback()
		else:
			logging.debug("执行修改SQL->%s,影响行数->%s"%(sql,result))
			return result
	def close(self):
		logging.debug("断开数据库链接")
		self.cur.close()
		self.conn.close()
# db = MySql(host="localhost",user="root",password="123456",db="taki_test")
# print(db.query("SELECT count(*) FROM stu"))
# db.close()




