const redis = require('redis');
const client = redis.createClient();

const { promisify } = require('util');
const getAsync = promisify(client.HGETALL).bind(client);

const setDataToHashTable = (data, hashkey) => {
    for (const [k, v] of Object.entries(data)) {
        client.hset(hashkey, k, v, redis.print)
    }
};

const getDataFromHashTable = async (hashkey) => {
    const getAllData = await getAsync(hashkey);
    console.log(getAllData);
}

const hashkey = 'HolbertonSchools';
const data = {
  Portland: 50,
  Seattle: 80,
  'New York': 30,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
  ABC: 3
};

setDataToHashTable(data, hashkey);
getDataFromHashTable(hashkey);