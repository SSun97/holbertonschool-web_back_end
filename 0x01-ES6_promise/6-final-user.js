/* eslint-disable no-param-reassign */

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((result) => {
      result[1].value = `Error: ${result[1].reason.message}`;
      delete result[1].reason;
      return result;
    });
}
