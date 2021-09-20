export default function getListStudentIds(arrobj) {
  if (!Array.isArray(arrobj)) {
    return [];
  } else {
    let ids = arrobj.map(x => x.id);
    return ids;
  } 
}
