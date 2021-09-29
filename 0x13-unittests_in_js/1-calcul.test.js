const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function() {
  it('checks valid output according to the operation type', function() {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
  it('checks output with negative numbers according to the operation type', function() {
    assert.strictEqual(calculateNumber('SUM', 2.8, -2.7), 0);
    assert.strictEqual(calculateNumber('SUM', -2.4, -2), -4);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, -1), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', -2, -2.1), 0);
    assert.strictEqual(calculateNumber('DIVIDE', -2.6, -2.6), 1);
    assert.strictEqual(calculateNumber('DIVIDE', -2, 0.2), 'Error');
  });
  it('checks arguments presence', function() {
    assert.strictEqual(isNaN(calculateNumber('SUM', 2)), true);
    assert.strictEqual(isNaN(calculateNumber('SUBTRACT', 2)), true);
    assert.strictEqual(isNaN(calculateNumber('DIVIDE', 2)), true);
    assert.strictEqual(isNaN(calculateNumber(1, 2)), true);
    assert.strictEqual(isNaN(calculateNumber()), true);
  });
});
