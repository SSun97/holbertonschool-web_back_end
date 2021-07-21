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
  const student5 = students(5, 'Serena', 'San Francisco');

  const studentList = [];
  studentList.push(student1, student2, student5);
  return studentList;
}
