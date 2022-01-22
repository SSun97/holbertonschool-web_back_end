const EventEmitter = require('events'); // It's a class

class Logger extends EventEmitter{
    log(message) {
        // send an HTTP request
        console.log(message);
        // Raise an event
        this.emit('messageLogged', {id: 1, url: 'http://'}); // Making a noise, something happened
    }
}
module.exports = Logger;