# -*- coding: utf-8 -*-
import urllib

def urldecode(link):
	decodes = {}
	if '?' in link:
		params = link.split('?')[1]
		for param in params.split('&'):
			k, v = tuple(param.split('='))
			decodes[k] = urllib.unquote(v)
		return decodes

def urlencode(params):
	return urllib.urlencode(params)