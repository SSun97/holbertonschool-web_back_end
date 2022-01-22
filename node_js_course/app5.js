const os = require('os');

var totalMemory = os.totalmem();
var freeMemory = os.freemem();
// console.log('Total Memory: ' + totalMemory);

// Template string
// ES6: ECMAScrtipt 6

console.log(`Total Memory: ${totalMemory}`);
console.log(`Total Memory: ${freeMemory}`);