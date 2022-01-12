const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('test sendPaymentRequestToApi flow', () => {
  const sendPaymentSpy = sinon.spy(sendPaymentRequestToApi);
  const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  const consoleLogSpy = sinon.spy(console, 'log');

  const totalAmount = sendPaymentRequestToApi(100, 20);

  it('validate if the sendPaymentRequestToApi reieved the correct inputs sent', () => {
    expect(sendPaymentSpy.calledWithExactly(100, 20));
  });
  it('validate wheth if the calculateNumber method received the correct inputs', () => {
    expect(calculateNumberSpy.calledWithExactly('SUM', 100, 20));
  });
  it('validate return value from total sendPaymentRequestToApi', () => {
    expect(totalAmount).to.be.equal(120);
  });
  it('validate wheth if the console.log executed and printed the correct string', () => {
    expect(consoleLogSpy.calledWithExactly('The total is: 120'));
  });
});
