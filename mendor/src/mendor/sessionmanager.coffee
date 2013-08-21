require './workermanager'



class SessionManager
	instance = undefined

	class Internal
		constructor: () ->
			@workermanager = WorkerManager()
			return

		#make sure be async
		start: (uid) ->
			return

		stop: (uid) ->
			return

	@get: () ->
		instance ?= Internal()







module.exports = SessionManager
