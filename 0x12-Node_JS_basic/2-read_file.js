const fs = require('fs');

const countStudents = (filePath) => {
  try {
    let data = fs.readFileSync(filePath, 'utf8').toString().split('\n');
    const studentsArray = data.slice(1, data.length - 1);
    console.log(`Number of students: ${studentsArray.length}`);
    const rows = {};
    for (const row of studentsArray) {
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
