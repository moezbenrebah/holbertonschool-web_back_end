export default function getStudentIdsSum(arrObj) {
  return arrObj.reduce((sum, { id }) => sum + id, 0);
}
