const fs = require('fs');

const countStudents = (filePath) => {
  try {
    let data = fs.readFileSync(filePath, 'utf8').toString().split('\n');
    data = data.slice(1, data.length - 1);
    console.log(`Number of students: ${data.length}`);
    const rows = {};
    for (const row of data) {
      const line = row.split(',');
      if (!rows[line[3]]) rows[line[3]] = [];
      rows[line[3]].push(line[0]);
    }
    for (const cls in rows) {
      if (cls) console.log(`Number of students in ${cls}: ${rows[cls].length}. List: ${rows[cls].join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
module.exports = countStudents;
