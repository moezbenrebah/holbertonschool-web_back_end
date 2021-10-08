import { createClient } from 'redis';
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client is connected to the server')
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.toString}`)
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (error, reply) => {
        redis.print(`Reply: ${reply}`);
    });
}

const displaySchoolValue = async (schoolName) => {
    const reply = await promisify(client.get).bind(client);
    console.log(reply);
}


(await () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}) ();
