#encoding: utf-8

from factory.workers.login import login
import base64
import re
import json
import binascii
import urllib
import urllib2
import rsa

class weibologin(login):
    def __init__(self,username,pwd):
        self.task = "weibo" #must be declared before super __init__
        super(weibologin,self).__init__(username,pwd)

    def __get_login_data(self):
        login_data = {
            'entry': 'weibo',
            'gateway': '1',
            'from': '',
            'savestate': '7',
            'userticket': '1',
            'ssosimplelogin': '1',
            'vsnf': '1',
            'vsnval': '',
            'su': '',
            'service': 'miniblog',
            'servertime': '',
            'nonce': '',
            'pwencode': 'rsa2',
            'sp': '',
            'rsakv':'1330428213',
            'encoding': 'UTF-8',
            'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype': 'META'
        }
        servertime_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.4)'
        login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.4)'
        return login_data, servertime_url, login_url
    
    def __get_rsa_mat(self,data):
        p = re.compile('\((.*)\)')
        try:
            json_data = p.search(data).group(1)
            data = json.loads(json_data)
            servertime = str(data['servertime'])
            nonce = data['nonce'].encode('UTF-8')
            pubkey = data['pubkey'].encode('UTF-8')
            rsakv = data['rsakv'].encode('UTF-8')
            return servertime, nonce, pubkey, rsakv
        except Exception, e:
            print e
            print 'Get severtime and pubkey error!'
            return 0, 0, 0, 0
        
    def __get_rsa_username_pwd(self,pubkey,servertime,nonce):
        uname = urllib.quote(self.uname) #encode url
        uname = base64.encodestring(uname)[:-1] #base64 encrypt username
        
        rsaPublickey = int(pubkey, 16)
        key = rsa.PublicKey(rsaPublickey, 65537) #create pubkey
        message = servertime + '\t' + nonce + '\n' + self.passwd #enc
        passwd = rsa.encrypt(message, key) #enc
        passwd = binascii.b2a_hex(passwd) #to oct
        
        return uname, passwd
    
    def __real_login(self,content):
        p = re.compile('location\.replace\(\"(.*?)\"\)')
        login_url = p.search(content).group(1)
        result,ts = self.get_html(login_url, False)
        try:
            p = re.compile('\((.*)\)')
            json_data = p.search(result).group(1)
            data = json.loads(json_data)
            result = str(data['result'])
            #print result
            if result == 'True':
                print 'RSA Login success!'
                #print self.cookie_file
                self.cookie_jar.save(self.cookie_file,ignore_discard=True, ignore_expires=True)
                return 1
            else:
                print 'ID is down!'#
                return 0
        except:
            print 'big problem, research new login method'
            return 0
    
    def do_login(self):
        login_data,servertime_url, login_url = self.__get_login_data()
        data,ts = self.get_html(servertime_url,False)
        servertime, nonce, pubkey, rsakv  = self.__get_rsa_mat(data)
        if servertime == 0:
            return 0

        uname, passwd = self.__get_rsa_username_pwd(pubkey, servertime, nonce)
        
        login_data['servertime'] = servertime
        login_data['nonce'] = nonce
        login_data['su'] = uname
        login_data['sp'] = passwd
        login_data['rsakv'] = rsakv
        login_data = urllib.urlencode(login_data)
   
        req_login  = urllib2.Request(
            url = login_url,
            data = login_data
        )
        result, ts= self.get_html(req_login, False)
   
        return self.__real_login(result)

    def cookie_login(self):
        url='http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack'
        text,ts = self.get_html(url,False)
        #print text.decode("GBK").encode('UTF-8')
        try:
            p = re.compile('\((.*)\)')
            json_data = p.search(text).group(1)
            data = json.loads(json_data)
            result = str(data['result'])
            if result:
                print 'Cookies login success!'
                self.cookie_jar.save(self.cookie_file,ignore_discard=True, ignore_expires=True)
                return 1
            else:
                return -1
        except:
            print 'Cookie part expired!'#cookie expires
            p = re.compile('location\.replace\(\"(.*?)\"\)')
            login_url = p.search(text).group(1)
            #print login_url
            if login_url:
                data = self.get_html(login_url, False)
                #print data
                p = re.compile('\((.*)\)')
                try:
                    json_data = p.search(data).group(1)
                    data = json.loads(json_data)
                    result = str(data['result'])
                    if result:
                        print 'Again cookie login success!'
                        self.cookie_jar.save(self.cookie_file,ignore_discard=True, ignore_expires=True)
                        return 1
                    else:
                        print 'Cookie error!'
                        return -1
                except:
                    return -1

    def check_login(self,url):
        if url == None or url.strip() == "":
            return -1
        if url.strip().startswith('http://weibo.com/login.php'):
            return -1
        return 1
        