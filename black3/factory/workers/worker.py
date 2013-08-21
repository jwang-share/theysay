#coding=utf-8

from factory.supports.memdb import memdb
import random
#from factory.supports.logger import logger

class worker(object):
	def __init__(self,openers,task_dispatcher,result_handler=None):
		self.task_dispatcher = task_dispatcher
		self.result_handler = result_handler
		self.openers = openers
		self.mdb = memdb()
		self.worker_name = self.get_worker_name()
		self.mdb.dict_update(self.worker_name,'IDLE')
		self.canrun = True
		pass

	def get_status(self):
		return self.status

	def get_worker_name(self):
		raise 'not implemented'

	def run(self):
		self.mdb.dict_update(self.worker_name,'BUSY')
		while True:
			task = self.task_dispatcher()
			if task == None:
				self.mdb.dict_update(self.worker_name,'IDLE')
				break
			self.do_run(task)

	def do_run(self):
		raise 'not implemented'

	def stop_run(self):
		self.canrun = False

	def get_html(self,url):
		while self.canrun:
			opener = self.get_opener()
			if opener == -1:
				return -1, -1
			content,ts = opener.get_html(url)
			if content == -1:
				return -1, -1
			if content == 0:
				print "get nothing..."
				opener.set_status(-1)
				continue
			return content, ts

	def get_opener(self):
		if self.openers == None:
			#logger.logger_error("no opener")
			print "no openers..."
			return -1
		num = len(self.openers)
		if num == 1:
			if openers[0].get_status() == 1:
				return openers[0]
			else:
				return -1
		else:
			index = random.randint(0,num-1)
			if self.openers[index].get_status() == -1:
				return openers[index]
			else:
				for opener in self.openers:
					if opener.get_status() == 1:
						return opener
				return -1