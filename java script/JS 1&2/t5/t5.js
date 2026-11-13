'use strict';

const year = Number(prompt('Enter a year:'));
let isLeap = false;

if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
  isLeap = true;
}

if (isLeap) {
  document.querySelector('#target').textContent = `${year} is a leap year.`;
} else {
  document.querySelector('#target').textContent = `${year} is not a leap year.`;
}
