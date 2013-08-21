#coding=utf-8

import threading
import time
import urllib2
import os
import sys
from supports.singletonmaker import singleton

"""
worker:
    weibo:"busy"
"""
@singleton
class keepalive(threading.Thread):
	def __init__(self,name,inteval):
		self.name = name
		self.url  = setting.KEEPALIVE_URL_PREFIX + name
		self.thread_stop = False
		selt.inteval = inteval
		pass
    
    def run(self):
    	while(not self.thread_stop):
    		send_heartbeat()
    		print time.ctime() + ": send a heatbeat to scheduler"
    		time.sleep(self.inteval)
    
    def kill(self):
    	self.thread_stop = True

  
    #worker needs a feedback?
	def send_heartbeat():
		data = {
		mem: "1024",
		usage: "512"
		}
		req = urllib2.Request(self.url, data=data)
		req.get_method = lambda: 'PUT'
		response = urllib2.urlopen(req)

