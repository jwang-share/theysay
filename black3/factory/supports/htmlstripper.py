#coding=utf-8

from logger import logger

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise DependencyNotInstalledError('BeautifulSoup4')

from HTMLParser import HTMLParser

class htmlstripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []

	def handle_data(self, data):
		self.fed.append(data)

	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	mlstripper = htmlstripper()
	mlstripper.feed(html)
	return mlstripper.get_data()