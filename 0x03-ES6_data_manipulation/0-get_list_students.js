export default function getListStudents() {
  function students(id, firstName, location) {
    return {
      id,
      firstName,
      location,
    };
  }
  const student1 = students(1, 'Guillaume', 'San Francisco');
  const student2 = students(2, 'James', 'Columbia');
  const student3 = students(3, 'Serena', 'San Francisco');

  const studentList = [];
  studentList.push(student1, student2, student3);
  return studentList;
}
