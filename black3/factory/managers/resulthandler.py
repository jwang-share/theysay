#coding=utf-8

import threading
import time
import urllib2
import os
import sys
from factory.supports.memdb import memdb
from rootcfg import RESULT_URL_PREFIX


class resulthandler(threading.Thread):
	def __init__(self):
		self.result = RESULT_URL_PREFIX
		self.mdb = memdb()
		pass

	def run(self):
		self.send_results()
		pass

	def send(self,uid,taskname, data):
		httpdata = {
		"uid": uid,
		"tname":taskname,
		"data": data
		}
		req = urllib2.Request(self.url, data=httpdata)
		req.get_method = lambda: 'PUT'
		response = urllib2.urlopen(req)
		pass

	def send_results(self):
		while True:
			store = self.mdb.get_store()
			dockeys = store.keys()
			for key in dockeys:
				substr = key.split('!')
				if substr[-1] != 'RESULT' || len(substr) < 3:
					continue
				result = self.mdb.popdoc(key)
				taskid = substr[-2]
				taskname = substr[0]
				self.send(taskid,taskname,result)
			time.sleep(60)



