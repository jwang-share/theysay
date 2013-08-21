# Configuration

global.config = {
	LOG_LEVEL: "info",
	LISTEN_PORT: 50050,
}

global.Async        = require 'async'
global.Step         = require 'step'
global.logger       = new (require './logger')("mendor")





