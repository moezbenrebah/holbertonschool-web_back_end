export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  let result = weakMap.get(endpoint);

  if (result) {
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  } else {
    weakMap.set(endpoint, 1);
  }

  if (result >= 5) {
    throw Error('Endpoint load is high');
  }
}
