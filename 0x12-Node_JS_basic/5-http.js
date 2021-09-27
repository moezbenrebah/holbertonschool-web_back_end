const http = require('http');
const countStudents = require('./3-read_file_async');


const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('content-type', 'text/plain');

  if (url === '/') {
    res.write('Hello Holberton School!');
  }

  if (url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const students = await countStudents(DATABASE);
      res.end(`${students.join('\n')}`);
    } catch (error) {
      res.end(error.message);
    }
  }
});

app.listen(1245, () => console.log('Server is running...');

module.exports = app;
