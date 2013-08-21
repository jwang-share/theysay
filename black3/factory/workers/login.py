#encoding: utf-8

"""

"""

import os
import urllib
import urllib2
import cookielib
from gzip import GzipFile
from StringIO import StringIO
import zlib
import base64
import re
import json
import binascii
import time
from rootcfg import ROOTDIR,CFG_DIR

class ContentEncodingProcessor(urllib2.BaseHandler):
    """A handler to add gzip capabilities to urllib2 requests """

    # add headers to requests
    def http_request(self, req):

        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22')
        req.add_header("Accept-Encoding", "gzip, deflate")
        return req

    # decode
    def http_response(self, req, resp):
        old_resp = resp
        # gzip
        if resp.headers.get("content-encoding") == "gzip":
            gz = GzipFile(
                    fileobj=StringIO(resp.read()),
                    mode="r"
                )
            resp = urllib2.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)
            resp.msg = old_resp.msg
        # deflate
        if resp.headers.get("content-encoding") == "deflate":
            gz = StringIO( deflate(resp.read()) )
            resp = urllib2.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)  # 'class to add info() and
            resp.msg = old_resp.msg
        return resp

# deflate support
def deflate(data):   # zlib only provides the zlib compress format, not the deflate format;
    try:               # so on top of all there's this workaround:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)

class login(object):

    encoding_support = ContentEncodingProcessor
    def __init__(self,username,pwd):# init urllib2 with cookie
        self.uname = username
        self.passwd = pwd
        cookie_file = CFG_DIR+self.task+'/'+username+".dat"
        self.cookie_file = cookie_file
        self.status = 1
        #httpHandler = urllib2.HTTPHandler(debuglevel=1)
        #httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
        self.cookie_jar = cookielib.MozillaCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(self.cookie_jar)
        self.opener = urllib2.build_opener(cookie_support, self.encoding_support,urllib2.HTTPHandler)
        urllib2.install_opener(self.opener)

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

      
    #normally, during login, set check_login to be False 
    def get_html(self,url,check_login=True):
        count = 0
        logincount = 0
        while True:
            try:
                if logincount > 5:
                    return 0, 0
                response = self.opener.open(url)
                if check_login == True:
                    res_url = response.geturl()
                    if self.check_login(res_url) == 1:
                        result = response.read()
                        ts = response.info()['date']
                        return result, ts
                    else:
                        self.login()
                        logincount += 1
                        if logincount > 1:
                            time.sleep(5)
                else:
                    result = response.read()
                    ts = response.info()['date']
                    return result, ts
            except:
                count += 1
                print "try to get html: " + str(count)
                if count > 5:
                   print "fail to get any content from website"
                   return -1, -1
                else:
                   time.sleep(5)

    def do_login(self):#login with RSA
        return -1

    def cookie_login(self):
        return -1

    def check_login(self,url):
        return -1

    def login(self):#login with cookie, mostly
        if os.path.exists(self.cookie_file):
            try:
                print "cookie login..."
                cookie_load = self.cookie_jar.load(self.cookie_file,ignore_discard=True, ignore_expires=True)
                if  self.cookie_login()  == 1:
                    return 1
                else:
                    print "turn to use account login"
                    return self.do_login()
            except cookielib.LoadError:
                print 'Loading cookies error'
                return self.do_login()
        else:
            print "account login..."
            return self.do_login()