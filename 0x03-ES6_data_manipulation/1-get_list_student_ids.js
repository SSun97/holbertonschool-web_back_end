export default function getListStudentIds(studentList) {
  if (!Array.isArray(studentList)) return [];
  let idList = [];
  idList = studentList.map((element) => element.id);
  return idList;
}
