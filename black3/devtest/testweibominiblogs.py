#!/usr/bin/env python
#coding=utf-8

import sys
sys.path.append('../')

from factory.supports.memdb import memdb
from factory.managers.weibomanager import weibominiblogmanager
if sys.getdefaultencoding() != "utf-8":
    reload(sys)
    sys.setdefaultencoding('utf-8')


if __name__ == "__main__":
	task = 'miniblogs'
	mdb = memdb()
	docname = 'weibo_'+task+'!TASK'
	print docname
	#tasks = ['3310333102']
	tasks = [('2482256271','0')]
	mdb.push(docname,tasks)
	worker_status = mdb.dict_show('weibo')
	if worker_status != "BUSY":
		if task == "followers":			
			wf = weibofollowmanager().start()
			pass
		elif task == "miniblogs":
			wm = weibominiblogmanager().start()
			pass
	print "---------------"