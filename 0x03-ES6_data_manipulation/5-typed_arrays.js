// https://www.youtube.com/watch?v=UYkJaW3pmj0
export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const dv1 = new DataView(buffer);
  dv1.setInt8(position, value);
  return dv1;
}
