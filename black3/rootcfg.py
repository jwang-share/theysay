from os import path


ROOTDIR = path.dirname(__file__)
LOGGER_DIR = path.dirname(__file__) + "/factory/logs/"
CFG_DIR = path.dirname(__file__)+"/factory/cfg/"
RELATION_PREFIX = '<script>STK && STK.pageletM && STK.pageletM.view({"pid":"pl_relation_myfollow","js":["home/js/pl/relation/follow/index.js?version='
HIS_FOLLOW_PREFIX = '<script>STK && STK.pageletM && STK.pageletM.view({"pid":"pl_relation_hisFollow","js":["home/js/pl/relation/hisFollow/index.js?version='
MY_FOLLOWERS_PAGE = 'http://weibo.com/3024695227/myfollow?t=1&page='
FOLLOW_URL_PREFIX = 'http://weibo.com/'
FOLLOW_URL_POSTFIX = '/follow?from=profile&wvr=5&loc=tagfollow'
COMMON_URL_PREFIX = 'http://weibo.com/'
HIS_FOLLOW_POSTFIX = '/follow?page='
HIS_ORIGIN_BLOG_PREFIX = 'http://www.weibo.com/aj/mblog/mbloglist?_wv=5&profile_ftype=1&is_ori=1'


KEEPALIVE_URL_PREFIX = ''
RESULT_URL_PREFIX = ''

BLOG_NUM_PER_BLOCK = 15
MAX_PAGE_NUM_PER_USER = 60000
WEBSERVER_HOST = '127.0.0.1'
WEBSERVER_PORT = 50050