#coding=utf-8

"""
"""
from rootcfg import  LOGGER_DIR, CFG_DIR
import ConfigParser

def save_to_disk(filename,content):
	if content == None:
		print "the content is none"
		return 0
	else:
		if type(content) != str:
			content = str(content)
			if len(content.strip) < 1:
				print "the content is none"
				return 0
	try:
		file_object = open(LOGGER_DIR+"/"+filename, 'w')
		file_object.write(content)
		file_object.close()
		return 1
	except Exception, e:
		print "error: " + str(e)
		return -1
	
def get_accounts(name):
	cf = ConfigParser.ConfigParser()
	cf.read(CFG_DIR+'accounts.cfg')
	#print cf.items(name)
	return cf.items(name)