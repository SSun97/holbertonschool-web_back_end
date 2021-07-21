export default function getStudentsByLocation(students, location) {
  return students.filter((element) => element.location === location);
}
