#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from factory.supports import format
from factory.supports.parser import parser
from factory.supports import htmlstripper
from weibocommon import weibocommon
from rootcfg import HIS_ORIGIN_BLOG_PREFIX
from rootcfg import BLOG_NUM_PER_BLOCK
from rootcfg import MAX_PAGE_NUM_PER_USER
import time
import simplejson as json
import re

if sys.getdefaultencoding() != "utf-8":
    reload(sys)
    sys.setdefaultencoding('utf-8')



class weibominiblogs(weibocommon):
	def __init__(self,openers,task_dispatcher, result_handler=None):
		super(weibominiblogs,self).__init__(openers,task_dispatcher,result_handler)
		self.end_id = 0
		self.handler =  result_handler
		pass

	def __init_url(self, uid):
		params = {}
		params['count'] = '50'
		params['_t'] = '0'
		params['uid'] = uid
		params['__rnd'] = str(int(time.time() * 1000))
		params['_k'] = str(int(time.time() * (10**6)))
		init_url = '%s&%s'%(HIS_ORIGIN_BLOG_PREFIX, format.urlencode(params))
		return init_url

	def do_run(self,task):
		item = task
		uid = item[0]
		lastestmid = item[1]
		nxt_url= self.__init_url(uid)
		self.end_id = 0
		index = 0
		while True:
			max_id = self.__get_one_block_content(nxt_url,uid,lastestmid)
			if max_id < 1:
					break
			nxt_url = self.__get_next_url(nxt_url,self.end_id,max_id)
			index += 1
			if index > MAX_PAGE_NUM_PER_USER:
				break

	def __get_one_block_content(self,url,uid,lastestmid):
		ps = self.get_target(url)
		if ps == -1:
			return -1
		divs = ps.find_all('div', attrs={'class': 'WB_feed_type SW_fun '})
		if len(divs) == 0:
			print "no more miniblog"
			return 0
			
		for div in divs:
			retv_i = {}
			mid = div['mid']
			max_id = mid
			if not mid or mid == 0:
				continue
			if lastestmid >= mid:
				return 0 # no new miniblog

			retv_i['uid'] = uid
			if self.end_id == 0:
				self.end_id = mid
				retv_i['latest_mid'] = self.end_id
			content_div = div.find('div', attrs={'class': 'WB_text', 'node-type': 'feed_list_content'})
			imgs = div.find_all("img",attrs={"class":"bigcursor"})
			mbcontent =  htmlstripper.strip_tags(str(content_div)).decode('utf-8')

			mds = div.find_all("li",attrs={'action-type':'feed_list_media_vedio'})
			mdconent = []
			for md in mds:
				data = md['action-data']
				md_imgs = md.find_all('img')
				md_imgsrc = []
				for mdimg in md_imgs:
					md_imgsrc.append(mdimg['src'])
				mdcontent.append(data)
				mdcontent.append(md_imgsrc)
			imgssrc = []
			for img in imgs:
				imgssrc.append(img['src'])
			time_a = div.find("a",attrs={"class":"S_link2 WB_time","node-type":"feed_list_item_date"})
			time_str = time_a['title']
			retv_i['mid'] = mid
			retv_i['miniblog'] = mbcontent
			retv_i['imgs'] = imgssrc
			retv_i['timestamp'] = time_str
			retv_i['media_info'] = mdconent
			if self.handler != None:
				self.handler([retv_i])
		if len(divs) < BLOG_NUM_PER_BLOCK:
			max_id = 0
		return max_id

	def __get_next_url(self, url,end_id,max_id):
		#how to deal the end of the message
		params = format.urldecode(url)
		params['__rnd'] = str(int(time.time() * 1000))
		page = int(params.get('page', 1))
		pre_page = params.get('pre_page', 1)
		if 'pagebar' not in params:
			params['pagebar'] = '0'
			params['max_id'] = max_id
			count = 15
		elif params['pagebar'] == '0':
			params['pagebar'] = '1'
			params['max_id'] = max_id
			count = 15
		elif params['pagebar'] == '1':
			del params['pagebar']
			del params['max_id']
			pre_page = page
			page += 1
			count = 50
			end_msign=-1

		params['count'] = count
		params['page'] = page
		params['pre_page'] = pre_page

		next_url = '%s&%s'%(HIS_ORIGIN_BLOG_PREFIX, format.urlencode(params))
		return next_url

	def get_target(self,url,target_prefix=""):
		content, ts = self.get_html(url)
		if content == -1:
			return -1
		data = json.loads(content)['data']
		if data:
			try:
				ps = parser(data)
				return ps
			except Exception, e:
				print e
				return -1			
		else:
			return -1



		