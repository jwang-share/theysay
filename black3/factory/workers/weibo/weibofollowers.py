#coding=utf-8

from weibocommon import weibocommon
from factory.supports import htmlstripper
import rootcfg
import re
import time
from factory.supports.parser import parser
from factory.supports.logger import logger
from rootcfg import FOLLOW_URL_PREFIX 
from rootcfg import FOLLOW_URL_POSTFIX
from rootcfg import HIS_FOLLOW_PREFIX
from rootcfg import COMMON_URL_PREFIX
from rootcfg import HIS_FOLLOW_POSTFIX

import sys
if sys.getdefaultencoding() != "utf-8":
    reload(sys)
    sys.setdefaultencoding('utf-8')


class weibofollowers(weibocommon):
	def __init__(self,openers,task_dispatcher, result_handler=None):
		super(weibofollowers,self).__init__(openers,task_dispatcher,result_handler)
		self.index = 0
		self.people = 0
		self.handler = result_handler
		self.baduids = {}

	def __get_follow_url(self,uid):
		fl_url = FOLLOW_URL_PREFIX+uid+FOLLOW_URL_POSTFIX
		return fl_url

	def do_run(self,task):
		#/1749127163/follow?page=
		uid = task
		url = self.__get_follow_url(uid)
		print url
		ps = self.get_target(url,HIS_FOLLOW_PREFIX)
		if ps == -1:
			if uid in self.baduids:
				self.baduids[uid] += 1
				if self.baduids[uid] > 5:
					logger.logger_error("uid: %s cannot be parsed"%uid)
					if self.__check_baduid() == -1:
						return
			else:
				self.baduids[uid] = 1
			if self.baduids[uid] < 6:
				#self.uids.insert(0,uid)
				#FIXme, add the failed uid to memdb again, marked as failed
				pass
		else:
			pagenum = self.__get_page_num(ps)
			self.get_uids(ps)			
			self.parse_pages(uid,pagenum) #start from page2l

	def __check_baduid(self):
		#if all the uids in self.uids are in baduid, return -1, some are in return 0, none in return 1
		uidnum = 2
		baduidnum = len(self.baduids)
		if baduidnum == uidnum:
			return -1
		if baduidnum > 0:
			return 0
		if baduidnum == 0:
			return 1

	def parse_pages(self,uid,pagenum):
		#I don't think it's a good idea to usr mutiple threads here, so just leave it in the current process
		#page 1 should be parse directly
		self.people = self.people+1
		totalnum = pagenum
		if pagenum > 10:
			pagenum = 10 #weibo limitation
		if pagenum == -1:
			return -1
		for i in range(2,pagenum+1):
			url = COMMON_URL_PREFIX+uid+HIS_FOLLOW_POSTFIX+str(i)
			ps = self.get_target(url,HIS_FOLLOW_PREFIX) 
			self.get_uids(ps)
			print "+++++++apture: " + uid+" page: "+str(i) + " total: "+str(totalnum) + " people: " + str(self.people)

	def __get_page_num(self,ps):
		if (ps==None) or (ps==-1):
			return -1
		pages = ps.find("div",attrs={"class":"W_pages W_pages_comment","node-type":"pageList"})
		al = pages.find_all("a",attrs={"class":"page S_bg1"})
		if ((al==None) or (al=="") or (al==" ")):
			return 1
		pagenum = 0
		for a1 in al:
			if int(a1.string) > pagenum:
				pagenum = int(a1.string)
		return pagenum

	def get_uids(self,ps):		
		userbox = ps.find("ul",attrs={"class":"cnfList","node-type":"userListBox"})
		#usrlis = userbox.find_all("li",attrs={"class":"clearfix S_line1","action":"itemClick"})
		#to be more precise
		usrlis = ps.find_all("div",attrs={"class":"con_left"})
		retlist = []
		
		for user in usrlis:
			retv = {}
			a1 = user.find("a",attrs={"class":"W_f14 S_func1"})
			userid = a1['usercard'][3:]
			userhref = a1['href']
			usernick = htmlstripper.strip_tags(str(a1)).decode('utf-8')
			#a2 = user.find("i",attrs={"class":re.compile(ur"W_ico16 approve")}) #fix to use regex here		
			#approve
			#approve_co
			#regex does not work???
			usertype = ""
			a2 = user.find("i",attrs={"class":"W_ico16 approve"})
			if not a2:
				a2 = user.find("i",attrs={"class":"W_ico16 approve_co"})

			if a2:
				usertype = a2['title']

			a3 = user.find("i",attrs={"class":"W_ico16 member"})
			ismember = 0
			if a3:
				ismember = 1
			span1 = user.find("span",attrs={"class":"addr"})
			useraddr = htmlstripper.strip_tags(str(span1)).decode('utf-8')
			#
			fl_href = "/"+userid+"/follow"
			fs_href = "/"+userid+"/fans"
			#wb_href = userhref

			connect1 = user.find("div",attrs={"class":"connect"})
			a4 = connect1.find("a",attrs={"href":fl_href})
			fl_num = a4.string
			a5 = connect1.find("a",attrs={"href":fs_href})
			fs_num = a5.string
			a6 = connect1.find("a",attrs={"href":userhref})
			wb_num = a6.string
			info = user.find("div",attrs={"class":"info"})
			infotxt = ""
			if info:
				infotxt = info.string

			print "need photo"

			print "id: "+userid + ", nick: "+usernick+", href: "+userhref
			print "follower num: "+fl_num + ", fans num: "+fs_num+", weibo num: "+wb_num
			print "user addr: "+useraddr+" usertype: "+usertype
			print "info: "+infotxt
		
			retv['uid'] = userid
			retv['nick'] = usernick
			retv['href'] = userhref
			retv['follower_num'] = fl_num
			retv['fans_num'] = fs_num
			retv['miniblog_num'] = wb_num
			retv['address'] = useraddr
			retv['usertype'] = usertype
			retv['info'] = infotxt
			if self.handler != None:
				self.handler([retv])
			self.index = self.index+1
			print "----------------------------------"+str(self.index)

		



			
