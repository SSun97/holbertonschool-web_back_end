function valueInArray(number, array) {
  return new Set(array).has(number);
}
export default function hasValuesFromArray(set1, array2) {
  return array2.every((number) => valueInArray(number, [...set1]));
}
