export default function updateStudentGradeByCity(arrObj, city, newGrades) {
  return (arrObj.filter((a) => a.location === city)).map((infos) => {
    const hasGrade = newGrades.filter((curr) => curr.studentId === infos.id);
    if (hasGrade.length) {
      return { ...infos, grade: hasGrade[0].grade };
    }
    return { ...infos, grade: 'N/A' };
  });
}
