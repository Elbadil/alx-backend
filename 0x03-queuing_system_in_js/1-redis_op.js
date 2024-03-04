import { createClient } from 'redis';
import { print } from 'redis';

const client = createClient()
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'))


const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      print(`Reply: ${reply}`);
    }
  });
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      print(reply);
    }
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
