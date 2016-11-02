/**
 * What's a Perfect Power anyway? (5 kyu)
 *
 * https://www.codewars.com/kata/whats-a-perfect-power-anyway
 */

function isPP (n) {
  for (let k = 2; k <= Math.log2(n); k++) {
    let min = Infinity;
    for (let m of divisors(n)) {
      let e = Math.pow(m, k);
      min = Math.min(e, min);
      if (e === n) {
        return [m, k];
      }
    }
    if (min > n) {
      break;
    }
  }
  return null;
}

function divisors (n) {
  let result = [];
  for (let m = 2; m <= Math.floor(n / 2); m++) {
    if (n % m === 0) {
      result.push(m);
    }
  }
  return result;
}

const test = require('tape');

test('isPP', (t) => {
  t.deepEqual(isPP(4), [2, 2], '4 = 2^2');
  t.deepEqual(isPP(9), [3, 2], '9 = 3^2');

  t.is(isPP(5), null, "5 isn't a perfect number");
  t.is(isPP(28), null, "28 isn't a perfect number");
  t.is(isPP(1000001), null, "1000001 isn't a perfect number");

  let pps = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484];
  for (let pp of pps) {
    t.isNot(isPP(pp), null, `the number ${pp} is a perfect power`);
  }

  for (let i = 0; i < 100; ++i) {
    let m = 2 + (Math.random() * 0xff) | 0;
    let k = 2 + (Math.random() * Math.log(0x0fffffff) / Math.log(m)) | 0;
    let l = Math.pow(m, k);
    let r = isPP(l);
    if (r === null) {
      t.isNot(r, null, l + ' is a perfect power');
      break;
    } else if (Math.pow(r[0], r[1]) !== l) {
      t.is(Math.pow(r[0], r[1]), l, 'your pair (' + r[0] + ', ' + r[1] + ") doesn't work for " + l);
      break;
    }
  }

  for (let i = 0; i < 100; ++i) {
    let l = (Math.random() * 0x0000ffff) | 0;
    let r = isPP(l);
    if (r !== null && Math.pow(r[0], r[1]) !== l) {
      t.is(Math.pow(r[0], r[1]), l, 'your pair (' + r[0] + ', ' + r[1] + ") doesn't work for " + l);
      break;
    }
  }

  t.end();
});
