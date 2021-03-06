const chai = require('chai');
const expect = chai.expect;
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi function', function() {
  const spy = sinon.spy(console, 'log');

  it('validate the usage of the Utils function', function() {
    const stub = sinon.stub(Utils, 'calculateNumber');
    stub.withArgs('SUM', 100, 20).returns(10);
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('The total is: 10')).to.be.true;
    stub.restore()
    spy.restore();
  });
});
