const fs = require('fs');

function countStudents(filePath) {
  try {
    const data = fs.readFileSync(filePath, { encoding: 'utf8' }).toString().split('\n');
    const studentsArray = data.slice(1, data.length - 1);
    console.log(`Number of students: ${studentsArray.length}`);
    const rows = {};
    for (const row of studentsArray) {
      let newRow = row.split(',');
      if (!(rows[newRow[3]])) {
        rows[newRow[3]] = [];
      }
      rows[newRow[3]].push(newRow[0]);
    }
    
    for (const cls in rows) {
      if (cls) {
        console.log(`Number of students in ${cls}: ${rows[cls].length}. List: ${rows[cls].join(', ')}`);
      }
    }
      } catch (err) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
