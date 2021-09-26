const fs = require('fs');

async function countStudents(filePath) {
  try {
    const data = await fs.promises.readFile(filePath, { encoding: 'utf8' });
    const studentList = [];
    const arr = data.split(/\r?\n/);
    const fieldName = arr[0].split(',');
    const bodyContent = arr.slice(1);

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
