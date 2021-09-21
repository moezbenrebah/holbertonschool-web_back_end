export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0 || typeof set !== 'object') return '';

  const arr = [];

  set.forEach((item) => {
    if (item && item.startsWith(startString)) {
      arr.push(item.substring(startString.length));
    }
  });

  return arr.join('-');
}
