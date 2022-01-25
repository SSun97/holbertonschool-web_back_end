const mongoose = require('mongoose');

connectToDb()
    .then(result => console.log('Connected to DB.'))
    .catch(err => console.log(err));

async function connectToDb() {
    await mongoose.connect('mongodb://127.0.0.1:27017/mongo-exercises');
}

const courseSchema = new mongoose.Schema({
    name: { 
        type: String,
        required: true,
        minlength: 5,
        maxlength: 255,
    },
    category: {
        type: String,
        required: true,
        enum: ['web', 'mobile', 'network']
    },
    author: String,
    tags: {
        type: Array,
        validate: {
            validator(v) {
                return Promise.resolve(v && v.length > 1)
            },
            message: 'A course should have at least one tag'
        }
    },
    date: Date,
    // date: { type: Date, default: Date.now },
    isPublished: Boolean,
    price: {type: Number, integer: true,
    required: function() { return this.isPublished }, // cannot use arrow function since it hasnot "this" keyword
    min: 10,
    max: 200
}
});

const Course = mongoose.model('Course', courseSchema);

async function createCourse() {
    const course = new Course({
        name: 'Angular Course',
        author: 'Simon',
        tags: 'a',
        isPublished: true,
        category: 'network',
        price: 30
        // price: 18
    });
    try {
        const isValid = await course.validate();
        console.log(isValid);
    } catch (error) {
        console.log(error.message)
    }
    // const result = await course.save();
    // console.log(result);
}
createCourse()

// async function getCourses() {
//     return await Course
//     .find({ isPublished: true, tags: 'backend' })
//     .sort({ name: 1 })
//     .select({ name: 1, author: 1 });
// }

// async function updateCourse(id) {
//     // Approach: Query first, findByID(), Modify its properti, save()
//     // var id = new mongoose.Types.ObjectId(id);
//     const course = await Course.findById(id);
//     if(!course) {
//         console.log('Cannot find ID');
//         return;
//     }
//     course.isPublished = true;
//     course.author = 'Another Author';
//     // course.set({
//     //     isPublished: true,
//     //     author: 'Another Author'
//     // });
//     const result = await course.save();
//     console.log(result);
//     // Approach: update first, update directely, optionally: get the updated document
// }
// updateCourse('61ef5b9130c13f7a17e68576');
// async function run() {
//     // const courses = await getCourses();
//     const course = await updateCourse('5a68fde3f09ad7646ddec17e')
//     console.log(course);
// }

// run();
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