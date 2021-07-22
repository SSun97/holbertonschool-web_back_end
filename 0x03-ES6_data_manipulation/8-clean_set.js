export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') return '';

  return [...set].filter((el) => el)
    .filter((item) => item.startsWith(startString))
    .map((item) => item.substring(startString.length))
    .join('-');
}
