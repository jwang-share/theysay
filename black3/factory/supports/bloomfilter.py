#coding=utf-8

from rootcfg import ROOTDIR
from singletonmaker import singleton
import os

try:
	from pybloomfilter import BloomFilter
except Exception, e:
	print e
	raise e


@singleton
class bloomfilter(object):
	def __init__(self):
		self.filename = ROOTDIR+'/factory/cfg/filter.bloom'
		self.bf = self.__getbloomfilter()
		if self.bf == -1:
			self.bf = BloomFilter(100000, 0.001, self.filename)
		pass

	def __getbloomfilter(self):	
		if os.path.exists(self.filename):
			bf = BloomFilter.open(self.filename)
			return bf
		else:
			return -1

	def getinstance(self):
		return self.bf



