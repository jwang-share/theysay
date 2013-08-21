import logging
from rootcfg import  LOGGER_DIR
import os

#
#use singleton later
logger = None

#Don't call the function outside
def get_logger_level():
	return logging.DEBUG

#Don't call the function outside
def init_logger():
	if logger != None:
		return logger
	debug_level = get_logger_level()
	logfile = os.path.join(LOGGER_DIR, 'black3.log')
	logging.basicConfig(filename = logfile,level = debug_level, filemode = 'a', format = '%(asctime)s - %(levelname)s: %(message)s')
	logger = logging.getLogger('black3') 
	return logger

def logger_error(errinfo):
	mylogger = init_logger()
	mylogger.ERROR(errinfo)

def logger_warn(errinfo):
	mylogger = init_logger()
	mylogger.WARN(errinfo)

def logger_debug(errinfo):
	mylogger = init_logger()
	mylogger.DEBUG(errinfo)


