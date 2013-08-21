

express         = require 'express'
querystring     = require 'querystring'
Controller  = require('./controller')

class Server
  constructor: () ->
    @app = express()
    @controller = new Controller()
    @configure(@app)

  configure: (app) ->
    app.configure () ->
      app.use(express.cookieParser())
      app.use(express.bodyParser())
      app.use(express.methodOverride())
      app.use(app.router)
      app.use(express.static(__dirname + '/../../public'))
      app.use(express.errorHandler({ dumpExceptions: true, showStack: true }))
      app.set('views',__dirname + '/../../views')
      app.set('view engine', 'ejs')
      return

    # routes
    self = this
    for api in @controller.routes
      do (api) ->
        fn_handler = (req, res) -> 
          try
            self.controller[api.method](req, res)
          catch error
            res.json(error)
        app[api.http_method](api.path, fn_handler)
        logger.info("route: #{api.http_method.toUpperCase()} #{api.path} => #{api.method}")

    return # configure.

  

  start: (port=config.LISTEN_PORT) ->
    @app.listen(port)
    logger.info "Server is listening to #{port}"


module.exports = Server