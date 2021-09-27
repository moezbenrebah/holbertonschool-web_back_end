const fs = require('fs');

const countStudents = (path) => {
  try {
    let data = fs.readFileSync(path, 'utf8').toString().split('\n');
    data = data.slice(1, data.length - 1);
    console.log(`Number of students: ${data.length}`);
    const rows = {};
    for (const row of data) {
      const student = row.split(',');
      if (!rows[student[3]]) rows[student[3]] = [];
      subjects[student[3]].push(student[0]);
    }
    for (const cls in rows) {
      if (cls) console.log(`Number of students in ${cls}: ${subjects[cls].length}. List: ${subjects[cls].join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
module.exports = countStudents;
