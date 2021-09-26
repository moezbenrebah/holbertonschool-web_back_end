const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  let initParse = 'This is the list of our students\n';
  await countStudents(process.argv[2]).then((result) => {
    initParse += result;
    res.end(initParse)
  }).catch((error) => {
    res.end(`This is the list of our students\n${error.message}`);
  });
});

app.listen(1245, () => console.log('Server is running...'));

module.exports = app;
