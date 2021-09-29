const chai = require('chai');
const expect = chai.expect;
const getPaymentTokenFromAPI = require('./6-payment_token.js');


describe('test getPaymentTokenAPI', done => {
  it('test async function', (done) => {
    getPaymentTokenFromAPI(true)
      .then((resolve) => {
        expect(resolve).to.include({data: 'Successful response from the API' });
      done();
      })
      .catch((error) => done(error));
  }); 
});
