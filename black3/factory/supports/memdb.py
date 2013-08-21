#coding=utf-8

"""
*Currently, it's not a good idea to use redis here.
*it costs too much, it cannot bring enough benifits here
*in case the extends in future, encapsualting a list here
"""

from singletonmaker import singleton

"""
try:
	import redis
except Exception, e:
	print e
	raise e


@singleton
class memdb(object):
	def __init__(self):
		self.rds = redis.StrictRedis(host='localhost', port=6379, db=0)
		pass

	def getinstance(self):
		return self.rds
"""

@singleton
class memdb(object):
	def __init__(self):
		self.store = {}
		self.flat = {}
		#add a lock in the obj?
		pass

	def get_store(self):
		return self.store

	def get_flat(self):
		return self.flat

	def dict_update(self,name,newvalue):
		#in order to keep uniform
		if name in self.flat:
			self.flat[name] = newvalue
			return 1
		else:
			self.flat[name] = newvalue

	def dict_show(self,name):
		if name in self.flat:
			return self.flat[name]
		else:
			return None

	def push(self,name,content):
		if type(content) != list:
			return -1
		if name in self.store:
			ctlist = self.store[name]
			ctlist.extend(content)
			return 1
		else:
			ctlist = []
			ctlist.extend(content)
			self.store[name] = ctlist
			return 1

    #pop from head
	def hpop(self,name):
		if name in self.store:
			ctlist = self.store[name]
			if len(ctlist) > 0:
				item = ctlist.pop(0)
				return item
			else:
				return None
		else:
			return None

    #
	def hpopx(self,name,num):
		if name in self.store:
			ctlist = self.store[name]
			llen = len(ctlist)
			if llen > 0:
				if num > llen:
					num = llen
				x = ctlist[0:num]
				del ctlist[0:num]
				return x
			else:
				return None

	def popdoc(self,name):
		if name in self.store:
			ctlist = self.store.pop[name]
			return relist

	def cleandoc(self,name):
		if name in self.store:
			del self.store[name]





