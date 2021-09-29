const chai = require('chai');
const expect = chai.expect;
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi function', function() {
  const spy = sinon.spy(console, 'log');

  it('validate the usage of the Utils function', function() {
    const stub = sinon.stub(Utils, 'calculateNumber');
    stub.withArgs('SUM', 100, 20).returns(20);
    sendPaymentRequestToApi(100, 20);
    expect(spyConsole.calledOnce).to.be.true;
    expect(spyConsole.calledWith('The total is: 10')).to.be.true;
    stub.restore()
    spy.restore();
  });
});
