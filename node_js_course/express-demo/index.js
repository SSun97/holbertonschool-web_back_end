const startDebugger = require('debug')('app:startup');
const dbDebugger = require('debug')('app:db');
const config = require('config');

const logger = require('./middleware/logger_midFn');
const courses = require('./routes/courses');
const home = require('./routes/home');
const express = require('express');
const morgan = require('morgan');
const app = express();

app.set('view engine', 'pug'); //dont have to require it, auto load
app.set('views', './views');

app.use(express.json());
app.use(express.urlencoded({ extended: true}));
app.use(express.static('public'));
app.use('/api/courses', courses);
app.use('/', home);

// Configuration
console.log('Application Name: ' + config.get('name'));
console.log('Mail server: ' + config.get('mail.host'));
console.log('Mail Password: ' + config.get('mail.password'))

if(app.get('env') === 'development') {
    app.use(morgan('tiny'));
    startDebugger('Morgan enabled...');
}
dbDebugger('Connected to database...')
app.use(logger);
app.use((req, res, next) => {
    console.log('Authenticating...');
    next();
});
// PORT
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Listing port ${port}`);
});
