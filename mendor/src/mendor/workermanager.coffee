class Worker
	constructor: () ->
		@name = undefined
		@task = undefined #task name
		@id = undefined #uid
		@status = 'IDLE'
		@skillset = undefined
		@create_time = '' #default time here
		return

	set_name: (name) ->
		@name = name

	get_name: () ->
		return @name

	set_task: (task) ->
		@task = task

	get_task: () ->
		return @task

	get_id: () ->
		return @id

	set_status: (status) ->
		@status = status

	get_status: () ->
		return @status

	set_skillset: (skillset) ->
		@skillset = skillset

	get_skillset: () ->
		return @skillset


class WorkerManager
	instance = undefined

	class Internal
		constructor: () ->
			@workers = new Array()
			return

		register: () ->
			return #return workerobj

		remove: (uid) ->
			return

		get_user_by_id: (uid) ->
			return

		get_user_by_name: (name,start,num) ->
			return

		get_user_by_task: (task,start, num) ->
			return

		get_users: (task,start,num) ->
			return

		update_user: (uid, attr) ->
			return

	@get: ()->
		instance ?= new Internal()




module.exports = WorkerManager