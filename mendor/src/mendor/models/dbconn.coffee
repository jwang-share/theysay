mongoose = require 'mongoose'

#continue to use mongoose here....
#I don't know how to reuse a db obj, seems that the solutions from google is not fit for me...

class dbOne
	constructor: (uri) ->
		@dburi = uri

	createConn: ()->
		conn = mongoose.createConnection(uri)
		return conn


class dbConn
	instance = undefined	
	@getConn: (uri) ->
		instance ?= new dbOne()
		return instance.getConn(uri)

	class Internal
		constructor: () ->
			conn_arr = new Array()

		getConn: (uri) ->
			if uri in conn_arr
				return conn_arr[uri]
			else
				thedb = new dbOne(uri)
				theconn = thedb.createConn()
				conn_arr[uri] = theconn
				return theconn









