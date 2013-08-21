#coding=utf-8

from external.bottle import route
import threading
from manager import manager
from factory.workers.weibo.weibologin import weibologin
from factory.supports.utils import get_accounts
from factory.workers.weibo.weibominiblogs import weibominiblogs
from factory.workers.weibo.weibofollowers import weibofollowers



class weibomanager(manager):
	def __init__(self):
		super(weibomanager,self).__init__()
		pass

	def get_worker_name(self):
		return 'weibo'

	def login_opener(self,account,pwd):
		login = weibologin(account,pwd)
		login_status = login.login()
		if login_status:
			return login
		else:
			print "fail to login weibo"
			return -1


class weibofollowmanager(weibomanager):
	def __init__(self):
		super(weibofollowmanager,self).__init__()
		self.wf = None
		pass

	def start_work(self,openers):
		self.wf = weibofollowers(openers,self.get_task,self.handle_result)		
		self.wf.run()
		pass

	def get_task_name(self):
		return 'weibo_followers'

	def stop_work(self):
		if self.wf != None:
			self.wf.stop_run()

	def handle_result(self,results):
		for item in results:
			uid = item['uid']
			if uid in self.bf:
				continue
			else:
				self.bf.update(uid)
				self.push_result(uid,[item])


class weibominiblogmanager(weibomanager):
	def __init__(self):
		super(weibominiblogmanager,self).__init__()
		self.wm = None
		pass

	def start_work(self,openers):
		self.wm = weibominiblogs(openers,self.get_task,self.handle_result)		
		self.wm.run()
		pass

	def stop_work(self):
		if self.wm != None:
			self.wm.stop_run()

	def handle_result(self,results):
		for item in results:
			uid = item['uid']
			self.push_result(uid,[item])
		pass

	def get_task_name(self):
		return 'weibo_miniblogs'

