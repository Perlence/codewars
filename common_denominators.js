/**
 * Common Denominators (5 kyu)
 *
 * https://www.codewars.com/kata/common-denominators
 */

function convertFrac (array) {
  if (!array.length) return '';
  let denominators = array.map(([_, d]) => d);
  let common = denominators.reduce(lcm);
  return '(' + array.map(([n, d]) => [n * (common / d), common]).join(')(') + ')';
}

function lcm (a, b) {
  if (a === b && b === 0) return 0;
  return a * (b / gcd(a, b));
}

function gcd (a, b) {
  if (b > a) {
    let t = a;
    a = b;
    b = t;
  }
  while (b !== 0) {
    let t = a;
    a = b;
    b = t % b;
  }
  return a;
}

const test = require('ava');

test('lcm', (t) => {
  t.is(lcm(2, 3), 6);
});

test('convertFrac', (t) => {
  let lst = [[1, 2], [1, 3], [1, 4]];
  t.is(convertFrac([]), '');
  t.is(convertFrac(lst), '(6,12)(4,12)(3,12)');
});
