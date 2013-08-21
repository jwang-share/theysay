



class WeiboController
	constructor: () ->
		@route = [
			{"/weibo/:id/start",                http_method: "put",      method: "start_work"},
			{"/weibo/:id/stop",                 http_method: "put",      method: "stop_work"},
			{"/weibo/followers/results/:id",    http_method: "post",     method: "handle_fl_results"},
			{"/weibo/miniblogs/results/:id",    http_method: "post",     method: "handle_mb_results"},
			{"/weibo/followers/failure/:id",    http_method: "post",     method: "handle_fl_failure"},
			{"/weibo/miniblogs/failure/:id",    http_method: "post",     method: "handle_mb_failure"},
			{"/weibo/followers/error/:id",      http_method: "get",     method: "handle_fl_error"},
			{"/weibo/miniblogs/error/:id",      http_method: "get",     method: "handle_mb_error"}

		]
		return


	start_work: (req, res) ->
		return

	stop_work: (req, res) ->
		return

	handle_fl_results: (req, res) ->
		return

	handle_mb_results: (req, res) ->
		return

	handle_fl_failure: (req, res) ->
		return

	handle_mb_failure: (req, res) ->
		return

	handle_fl_error: (req, res) ->
		return

	handle_mb_error: (req, res) ->
		return


