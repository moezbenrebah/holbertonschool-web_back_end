const express = require('express');

const app = express();
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(1245, () => console.log('Server is Running...'));

module.exports = app;
