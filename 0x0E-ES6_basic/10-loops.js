export default function appendToEachArrayValue(array, appendString) {
  const a = [];
  for (let idx of array) {
    a.push(`${appendString}${idx}`);
  }

  return a;
}
