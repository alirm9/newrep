'use strict';

const shouldCalculate = confirm('Should I calculate the square root?');
const target = document.querySelector('#target');

if (shouldCalculate) {
  const num = Number(prompt('Enter a number:'));
  if (num < 0) {
    target.textContent = 'The square root of a negative number is not defined';
  } else {
    target.textContent = `The square root of ${num} is ${Math.sqrt(num)}.`;
  }
} else {
  target.textContent = 'The square root is not calculated.';
}
