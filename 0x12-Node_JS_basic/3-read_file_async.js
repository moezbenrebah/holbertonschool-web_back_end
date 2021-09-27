const fs = require('fs');

function countStudents(path) {
  const promise = (resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) reject(Error('Cannot load the database'));
      const messages = [];
      let message;
      const content = data.toString().split('\n');
      let students = content.filter((item) => item);
      students = students.map((item) => item.split(','));
      const nStudents = students.length ? students.length - 1 : 0;
      message = `Number of students: ${nStudents}`;
      console.log(message);
      messages.push(message);

      const fields = {};
      for (const i in students) {
        if (i !== 0) {
          if (!fields[students[i][3]]) fields[students[i][3]] = [];
          fields[students[i][3]].push(students[i][0]);
        }
      }
      delete fields.field;
      for (const key of Object.keys(fields)) {
        message = `Number of students in ${key}: ${
          fields[key].length
        }. List: ${fields[key].join(', ')}`;
        console.log(message);
        messages.push(message);
      }
      resolve(messages);
    });
  };
  return new Promise(promise);
}
module.exports = countStudents;
