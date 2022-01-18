const redis = require('redis');
const client = redis.createClient();

client.on('ready', () => console.log('Redis client connected to the server'));
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

const subConfirm = 'holberton school channel'
client.subscribe(subConfirm);
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(subConfirm);
    client.quit();
  }
})