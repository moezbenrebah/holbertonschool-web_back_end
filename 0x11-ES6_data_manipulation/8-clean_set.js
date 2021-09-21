export default function cleanSet(set, startString) {
  if (typeof startString !== 'string') return '';
  if (startString.length === 0) return '';
  if (typeof set !== 'object') return '';

  const arr = [];

  set.forEach((item) => {
    if (item.startsWith(startString)) {
      arr.push(item.substring(startString.length));
    }
  });

  return arr.join('-');
}
