const fs = require('fs');

function countStudents(filePath) {
  try {
    const data = fs.readFileSync(filePath, { encoding: 'utf8' }).split(/\r?\n/);
    const studentList = [];
    const fieldName = data[0].split(',');
    const bodyContent = data.slice(1);

    for (let i = 0; i < bodyContent.length; i += 1) {
      const result = bodyContent[i].split(',');
      if (result.length === fieldName.length) {
        const line = {};
        for (let j = 0; j < fieldName.length; j += 1) {
          line[fieldName[j].trim()] = result[j].trim();
        }
        studentList.push(line);
      }
    }

    let csClass = 0;
    let sweClass = 0;
    const cs = [];
    const swe = [];

    studentList.forEach((n) => {
      if (n.field === 'CS') {
        csClass += 1;
        cs.push(n.firstname);
      } else if (n.field === 'SWE') {
        sweClass += 1;
        swe.push(n.firstname);
      }
    });

    const countStudents = csClass + sweClass;

    console.log(`Number of students: ${countStudents}`);
    console.log(`Number of students in CS: ${csClass}. List: ${cs.toString().split(',').join(', ')}`);
    console.log(`Number of students in SWE: ${sweClass}. List: ${swe.toString().split(',').join(', ')}`);

  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
