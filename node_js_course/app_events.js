const Logger = require('./logger');
const logger = new Logger();

logger.on('messageLogged', (arg) => { // e, evenArg
    console.log('Listener called', arg);
});

logger.log('message');
