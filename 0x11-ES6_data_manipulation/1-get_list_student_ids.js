export default function getListStudentIds(arrobj) {
  if (!Array.isArray(arrobj)) {
    return [];
  }
  const ids = arrobj.map((x) => x.id);
  return ids;
}
