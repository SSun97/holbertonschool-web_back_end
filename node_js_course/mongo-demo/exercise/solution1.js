const mongoose = require('mongoose');

mongoose.connect('mongodb://127.0.0.1/mongo-exercises');

const courseSchema = new mongoose.Schema({
  _id: String,
  name: String,
  author: String, 
  tags: [ String ],
  date: Date, 
  isPublished: Boolean,
  price: Number
});

const Course = mongoose.model('Course', courseSchema);

async function getCourses() {
  return await Course
    .find({ isPublished: true })
    .or([{ price: { $gte: 15 } }, { name: /.*by.*/i }]);


  // .find({ isPublished: true, tags: 'backend' })
  // .sort({ name: 1 })
  // .select({ name: 1, author: 1 });
}

// async function updateCourse(id) {
//   const course = await Course.findByIdAndUpdate(id, { 
//     $set: {
//       author: 'Mosh1234',
//       isPublished: false
//     }
//   }, {new: true});
//   console.log(course);
// }
// updateCourse("5a68fde3f09ad7646ddec17e");
// console.log('Update done');


async function removeCourse(id) {
  const result = await Course.deleteOne({ _id: id });
  const result = await Course.deleteMany({ _id: id });
  const result = await Course.findByIdAndRemove(id);
  console.log(result);
}
removeCourse("5a68fde3f09ad7646ddec17e");

// async function run() {
//   // const courses = await getCourses();
//   const courses = await updateCourse('5a68fde3f09ad7646ddec17e');
//   console.log(courses);
// }

// run();
