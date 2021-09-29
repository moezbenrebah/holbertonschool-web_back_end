const Utils = require('./utils.js')

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const result = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The totalis: ${result}`);
}

module.exports = sendPaymentRequestToApi;
