const mongoose = require('mongoose');

connectToDb()
    .then(result => console.log('Connected to DB.'))
    .catch(err => console.log(err));

async function connectToDb() {
    await mongoose.connect('mongodb://127.0.0.1:27017/mongo-exercises');
}

const courseSchema = new mongoose.Schema({
    name: String,
    author: String,
    tags: [ String ],
    date: Date,
    // date: { type: Date, default: Date.now },
    isPublished: Boolean
});

const Course = mongoose.model('Course', courseSchema);

async function getCourses() {
    return await Course
    .find({ isPublished: true, tags: 'backend' })
    .sort({ name: 1 })
    .select({ name: 1, author: 1 });
}
async function run() {
    const courses = await getCourses();
    console.log(courses);
}

run();
    // async function getCourses() {
//     const courses = await Course
//         .find()
//         // .find({ isPublished: true })
//         // .find({ name: /.*Node.js.*/i })
//         // .sort({ name: 1 })
//         // .select({ name: 1, author: 1 });
//     console.log(courses);
// }
// getCourses();