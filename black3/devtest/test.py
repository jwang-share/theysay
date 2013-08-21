#!/usr/bin/env python
#coding=utf-8

import sys
sys.path.append('../')

from factory.supports.memdb import memdb
from factory.managers.weibomanager import weibofollowmanager


if __name__ == "__main__":
	task = 'followers'
	mdb = memdb()
	docname = 'weibo_'+task+'!TASK'
	print docname
	#tasks = ['3310333102']
	tasks = ['2482256271']
	mdb.push(docname,tasks)
	mdb1 = memdb()
	worker_status = mdb.dict_show('weibo')
	if worker_status != "BUSY":
		if task == "followers":			
			wf = weibofollowmanager().start()
			pass
		elif task == "miniblog":
			wm = weibominiblogmanager().start()
			pass
	print "---------------"
