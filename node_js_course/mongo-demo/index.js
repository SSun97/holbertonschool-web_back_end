const mongoose = require('mongoose');

main()
    .then(result => console.log('connected'))
    .catch(err => console.log(err));

async function main() {
  await mongoose.connect('mongodb://127.0.0.1:27017/playground');
}

const courseSchema = new mongoose.Schema({
    name: String,
    author: String,
    tags: [ String ],
    date: { type: Date, default: Date.now },
    isPublished: Boolean
});

const Course = mongoose.model('courses', courseSchema);

async function createCourse() {

    const course = new Course({
        name: 'Angular Course',
        author: 'Mosh',
        tags: ['Angular', 'frontend'],
        isPublished: true
    });
    
    const result = await course.save();
    console.log(result);
}

async function getCourses() {
    const pageNumber = 1;
    const pageSize = 10;
    // /api/course?pageNumber=2
    // eq (equal) ne gt gte(greater than or equal to) lt lte in nin (not in)
    // or and 
    const courses = await Course
        .find({ author: 'Mosh', isPublished: true })
        // .find({ price: { $gte: 10, $lte: 20 } })
        // .find({ price: { $in: [10, 15, 20] } })
        // .find()
        // .or([ { author: 'Mosh' }, { isPublished: true } ])
        // .and([ { author: 'Mosh' }, { isPublished: true } ])
        // Starts with Mosh
        // .find({ author: /^Mosh/ })
        // .find({ author: /Hamedani$/i }) // i - case insensitive
        // .find({ author: /.*Mosh.*/i })
        .skip((pageNumber - 1) * pageSize)
        .limit(pageSize) //get the given page
        .sort({ name: 1 })
        // .select({ name: 1, tags: 1, author: 1 }); //or -1 decent
        .count()
    console.log(courses);
}

getCourses();