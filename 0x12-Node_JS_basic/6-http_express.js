const express = require('express');

const app = express();
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(port, () => console.log('Server is Running...'));

module.exports = app;
