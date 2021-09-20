export default function getStudentsByLocation(arrObj, city) {
  return arrObj.filter(x => x.location === city);
}
