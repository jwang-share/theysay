


class Controller
	constructor: () ->
		@routes = [
			{"/workers/keepalive/:id"      http_method: "put",         method: "keep_alive"},
			{"/worker/register",           http_method: "post",        method: "register_worker"},  
			{"/employee",                  http_method: "get",         method: "employ_worker"},
			{"/workers",                   http_method: "get",         method: "get_workers"}
		]
		return

	get_workers: (req,res) ->
		return

	keep_alive: (req, res) ->
		return

	employ_worker: (req, res) ->
		return

	register_worker: (req, res) ->
		return
    
 


module.exports = Controller
