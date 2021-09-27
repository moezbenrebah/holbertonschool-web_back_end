const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.set('content-type', 'text/plain');
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students') {
    let result = 'This is the list of our students\n';
    await countStudents(process.argv[2])
      .then((data) => {
        result += data;
        res.end(result);
      })
      .catch((error) => {
        result += error.message;
        res.end(result);
      });
  }
});

app.listen(1245, () => console.log('Server is running...');

module.exports = app;
