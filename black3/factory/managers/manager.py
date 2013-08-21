#coding=utf-8

import threading
from factory.supports.bloomfilter import bloomfilter
from factory.supports.memdb import memdb
from factory.supports.utils import get_accounts
try:
	import redis
except Exception, e:
	raise e

'''
worker status: IDLE, BUSY, DEAD
'''

class manager(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.bf = bloomfilter().getinstance()
		self.mdb = memdb()
		self.taskname = self.get_task_name()
		self.workername = self.get_worker_name()
		pass

	def start_work(self,openers):
		raise "not implemented"

	def get_openers(self):
		accounts = get_accounts(self.workername)
		if len(accounts) < 1:
			return []
		openers = []
		for account in accounts:
			print account[0]
			print account[1]
			oper = self.login_opener(account[0],account[1])
			if oper == -1:
				continue
			openers.append(oper)
		return openers

	def handle_result(self, result):
		raise "not implemented"

	def get_task_name(self):
		raise "not implemented"

	def get_worker_name(self):
		raise "not implemented"

	def get_worker_status(self):
		workername = self.get_worker_name()
		return self.memdb().dict_show(workername)

	def get_task(self,num=1):
		tasklistname = self.taskname+"!TASK"
		print self.mdb.store
		if num < 1:
			return -1
		if num == 1:
			item = self.mdb.hpop(tasklistname)
			print item
			return item
		else:
			return self.mdb.hpopx(tasklistname,num)
		
	def push_result(self,uid,content):
		resultlistname = self.taskname+"!"+uid+"!RESULT"
		self.mdb.push(resultlistname,content)


	def run(self):
		openers = self.get_openers()
		print "openers: "+str(len(openers))
		self.start_work(openers)
		pass
