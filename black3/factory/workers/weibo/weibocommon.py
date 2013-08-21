#coding=utf-8

#from factory.supports.logger import logger
from factory.workers.worker import worker
from factory.supports.utils import save_to_disk
from factory.supports.parser import parser


class weibocommon(worker):
	def __init__(self, openers, task_dispatcher, result_handler=None):
		super(weibocommon,self).__init__(openers,task_dispatcher,result_handler)
		pass

	def get_worker_name(self):
		return "weibo"

	def get_target(self,url,target_prefix=""):
		content, ts = self.get_html(url)
		if content == -1:
			return -1
		lines = content.splitlines()
		for line in lines:
			if line.startswith(target_prefix):
				n = line.find('html":"')
				target =  line[n+7:-12]
				target = target.replace("\\t","")
				target = target.replace("\\n","")
				target = target.replace("\\r",'')
				target = target.replace("\\",'')
				ps = parser(target)
				if ps == None:
					#logger.logger_error("bad content")
					print "why here..."
					return -1
				return ps
		#logger.logger_error("bad content, please check the resource")
		print "bad content, please check the resource"
		save_to_disk("tmp.html",content)
		return -1




