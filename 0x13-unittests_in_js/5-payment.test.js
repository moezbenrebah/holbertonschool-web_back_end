const chai = require('chai');
const expect = chai.expect;
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./5-payment.js');

describe('sendPaymentRequestToApi function', function() {
  let spy;
  beforeEach(function () { spy = sinon.spy(console, 'log'); });
  afterEach(function () { spy.restore(); });

  it('validate the usage of the Utils function', function() {
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('The total is: 120')).to.be.true;
  });

  it('validate the usage of the Utils function', function() {
    sendPaymentRequestToApi(10, 10);
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('The total is: 20')).to.be.true;
  });
});
