const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
  it('checks the sum of 2 rounded integers', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(1.7, 2), 4);
  });
  it('checks negative numbers output', function() {
    assert.strictEqual(calculateNumber(2, -2), 0);
    assert.strictEqual(calculateNumber(-2, 2), 0);
    assert.strictEqual(calculateNumber(2, -1), 1);
    assert.strictEqual(calculateNumber(-1, -2), -3);
  });
  it('checks arguments presence', function() {
    assert.strictEqual(isNaN(calculateNumber(2)), true);
    assert.strictEqual(isNaN(calculateNumber()), true);
  });
});
