# Configuration

global.config = {
	LOG_LEVEL: "info",
	LISTEN_PORT: 50050,
}

global.dbConfig = {
	WEIBO_ROSTER_URI: "",
	WEIBO_MINIBLOG_URI: "",
}

global.Async        = require 'async'
global.Step         = require 'step'
global.logger       = new (require './logger')("mendor")

global.Mongoose = require "mongoose"
global.Schema = Mongoose.Schema





