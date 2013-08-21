#coding=utf-8

"""
*in case using other parsers to replace BeautifulSoup
"""

try:
	from bs4 import BeautifulSoup
	pass
except Exception, e:
	logger.logger_error("Did not find BeautifulSoup")
	raise e

class parser(BeautifulSoup):
	def __init__(self, content):
		super(parser, self).__init__(markup=content)
		pass

	def find(self, name=None, attrs={}, recursive=True, text=None,**kwargs):
		return super(parser, self).find(name, attrs, recursive, text, **kwargs)
		

	def find_all(self, name=None, attrs={}, recursive=True, text=None,limit=None, **kwargs):
		return super(parser, self).find_all(name,attrs, recursive, text,limit, **kwargs)
		
