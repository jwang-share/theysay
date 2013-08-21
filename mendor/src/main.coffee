require './mendor/config'

console.log "main...."
console.log "mendor"

Server = require './mendor/server'
new Server().start()