const http = require('http');
const countStudents = require('./3-read_file_async');
const port = 1245;

const app = http.createServer((req, res) => {
  //res.statusCode = 200;
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  else if (req.url === '/students') {
    res.end(`This is the list of our students ${countStudents(process.argv[2])}`)
  }
});


app.listen(port, () => console.log('Server is running...'));
