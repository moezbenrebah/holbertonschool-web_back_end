export default function cleanSet(set, startString) {
  if (startString.length === 0) return '';

  const arr = [];

  set.forEach((item) => {
    if (item.startsWith(startString)) {
      arr.push(item.substring(startString.length));
    }
  });

  return arr.join('-');
}
