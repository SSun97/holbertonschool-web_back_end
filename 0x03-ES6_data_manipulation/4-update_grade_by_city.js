export default function updateStudentGradeByCity(students, city, newGrade) {
  const studentsByLocation = students.filter((element) => element.location === city);

  for (const item of studentsByLocation) {
    item.grade = 'N/A';
  }

  const updateGrade = studentsByLocation.map((element) => {
    //  error  Assignment to property of function parameter 'element'  no-param-reassign
    const elementCopy = element;

    for (const property of newGrade) {
      if (elementCopy.id === property.studentId) elementCopy.grade = property.grade;
    }
    return elementCopy;
  });
  return updateGrade;
}
