async function run() {
    const { createConnection, Schema } = require('mongoose');
    const connection = createConnection('mongodb://localhost:27017/test');
    const userSchema = new Schema({
      email: {
        type: String,
        validate: {
          validator(v) {
            return Promise.resolve(/(.+)@(.+){2,}.(.+){2,}/.test(v));
          },
          message: props => `${props.value} is not a email!`
        },
        required: [true, 'Email is required']
      }
    });
    const User = connection.model('User', userSchema);
    const user = new User();
    user.email = 'test';
    try {
      await user.validate();
    } catch (error) {
      console.log(error);
    }
  }
  run();