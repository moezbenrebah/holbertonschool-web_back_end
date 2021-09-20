export default function getListStudents() {
  const students = [];

  const student1 = {};
  student1.id = 1;
  student1.firstName = 'Guillaume';
  student1.location = 'San Francisco';
  students.push(student1);

  const student2 = {};
  student2.id = 2;
  student2.firstName = 'James';
  student2.location = 'Columbia';
  students.push(student2);

  const student3 = {};
  student3.id = 5;
  student3.firstName = 'Serena';
  student3.location = 'San Francisco';
  students.push(student3);

  return students;
}
