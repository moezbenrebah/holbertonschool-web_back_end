const request = require('request');
const chai = require('chai');
const expect = chai.expect;


describe('integration test', () => {
  describe('GET route', () => {
    it('endpoint', (done) => {
      const call = {
        url: 'http://127.0.0.1:7865',
        method: 'GET',
      };
      request(call, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
});
