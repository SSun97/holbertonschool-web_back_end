export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') return '';
  // const array = [...set].filter((el) => el);
  // const newArray = array.filter((item) => item.startsWith(startString));
  // const arrayAfterCut = newArray.map((item) => item.substring(startString.length));
  // const string = arrayAfterCut.join('-');
  // return string;

  return [...set].filter((el) => el)
    .filter((item) => item.startsWith(startString))
    .map((item) => item.substring(startString.length))
    .join('-');
}
