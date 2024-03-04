import { createClient } from "redis";
import { promisify } from "util";

const client = createClient()
  .on("error", (err) =>
    console.log(`Redis client not connected to the server: ${err}`)
  )
  .on("connect", () => console.log("Redis client connected to the server"));

// Promisifying the setNewSchool and displaySchoolValue functions
const asyncSet = promisify(client.set).bind(client);
const asyncGet = promisify(client.get).bind(client);

const setNewSchool = async (schoolName, value) => {
  try {
    const reply = await asyncSet(schoolName, value);
    console.log(`Reply: ${reply}`);
  } catch (err) {
    console.error(err);
  }
};

const displaySchoolValue = async (schoolName) => {
  try {
    const respValue = await asyncGet(schoolName);
    console.log(respValue);
  } catch (err) {
    console.error(err);
  }
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
