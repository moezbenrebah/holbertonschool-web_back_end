const chai = require('chai');
const expect =  chai.expect;
const calculateNumber = require('./2-calcul_chai.js');


describe('calculateNumber using operation type == SUM', function() {
  it('checks output', function() {
    expect(calculateNumber('SUM', 1.5, 3.2)).to.equal(5);
    expect(calculateNumber('SUM', 1.7, 3)).to.equal(5);
    expect(calculateNumber('SUM', 0.2, 3)).to.equal(3);
    expect(calculateNumber('SUM', 2.8, 3)).to.equal(6);
  })
});

describe('calculateNumber using operation type == SUBTRACT', function() {
  it('checks output', function() {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', -1, 3)).to.equal(-4);
    expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
    expect(calculateNumber('SUBTRACT', 1.5, -3.6)).to.equal(6);
    expect(calculateNumber('SUBTRACT', 3.9, 3.8)).to.equal(0);
    expect(calculateNumber('SUBTRACT', -1, 3)).to.equal(-4);
  })
});

describe('calculateNumber using operation type == DIVIDE', function() {
  it('checks output', function() {
    expect(calculateNumber('DIVIDE', 3, 3)).to.equal(1);
    expect(calculateNumber('DIVIDE', 1, 0.2)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 1.8, 2)).to.equal(1);
    expect(calculateNumber('DIVIDE', 2, -2)).to.equal(-1);
    expect(calculateNumber('DIVIDE', 2.2, 0.4)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 4.2, 2.1)).to.equal(2);
  })
});
