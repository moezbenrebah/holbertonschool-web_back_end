export default function getStudentIdsSum(arrObj) {
  if (arrObj.length !== 0) {
    return arrObj.reduce((sum, { id }) => sum + id, 0);
  }
}
