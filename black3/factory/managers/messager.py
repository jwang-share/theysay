

from external.bottle import Bottle, route, run, request
from managers.weibomanager import weibofollowmanager
from managers.weibomanager import weibominiblogmanager
from supports.memdb import memdb
#from supports.singletonmaker import singleton
 


def start_server():
	try:
		run(host="127.0.0.1", port=50050)
		pass
	except Exception, e:
		print e
		raise e	

#url format: /workername/:taskname
@route('/weibo/:task',method='POST')
def start_weibo_work(task):
	mdb = memdb()
	docname = 'weibo_'+task
	tasks = request.forms.get("tasks")
	mdb.push(docname,tasks)
	worker_status = mdb.dict_show('weibo')
	if worker_status != "BUSY":
		mdb.cleandoc(docname)
		if task == "followers":			
			wf = weibofollowmanager().start()
			pass
		elif task = "miniblog":
			wm = weibominiblogmanager().start()
			pass
	pass

@route('/weibo/:task',method='DELETE')
def kill_weibo_task(task):
	pass

@route('/weibo/:task', method='GET')
def get_weibo_task_info(task):
	pass

