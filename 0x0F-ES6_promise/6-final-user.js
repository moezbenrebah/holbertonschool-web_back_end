import signUpUser from './4-user-promise'
import  uploadPhoto from './5-photo-reject'

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUp = await signUpUser(firstName, lastName).then((data) => ({ status: 'fulfilled', value: data }));

  const photo = await uploadPhoto(fileName).catch((rerro) => ({ status: 'rejected', value: error.toString() }));

  return [signUp, photo];
}
