MongoClient = require('mongodb').MongoClient
Server = require('mongodb').Server

#continue to use mongoose here....
#I don't know how to reuse a db obj, seems that the solutions from google is not fit for me...


class dbOne
	contructor: (dburl) ->
		return



class dbConn
	instance = new Array()
	mongoclient = undefined

	class Internal
		contructor: (mc) ->
			db = undefined
			mongoclient = new MongoClient(new Server(dburl, dbport, {native_parser: true}))
			mongoclient.open (err, client) =>
			return
		getConn: () ->
			return @db

	@open: (dburl,dbport,dbname) ->
		fullurl = dburl+'\\'+dbport

		if fullurl in instance
			dbs = instance[fullurl].getConn()
			return dbs[dbname]
		else
			oneobj = Internal(dburl,dbport,dbname)
			instance[fullurl] = oneobj
			return oneobj.getConn()[dbname]
		return

	@close: (dburl) ->
		return