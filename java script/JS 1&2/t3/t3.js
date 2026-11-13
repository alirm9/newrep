'use strict';

const num1 = Number(prompt('Enter first integer:'));
const num2 = Number(prompt('Enter second integer:'));
const num3 = Number(prompt('Enter third integer:'));

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

document.querySelector('#target').innerHTML = `
  <p>Sum: ${sum}</p>
  <p>Product: ${product}</p>
  <p>Average: ${average}</p>
`;
