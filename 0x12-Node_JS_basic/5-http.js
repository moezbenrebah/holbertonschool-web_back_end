const http = require('http');
const countStudents = require('./3-read_file_async');
const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  else if (req.url === '/students') {
    let initParse = 'This is the list of our students\n';
    await countStudents(process.argv[2]).then((result) => {
      initParse += result;
      res.end(initParse)
    }).catch((error) => {
      initParse += error.message;
      res.end(initParse);
    });
  }
});

app.listen(port, () => {
  console.log('Server is running...');
});

module.exports = app;
