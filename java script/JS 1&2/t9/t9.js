'use strict';

const num = Number(prompt('Enter an integer:'));
let isPrime = true;

if (num <= 1) {
  isPrime = false;
} else {
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      isPrime = false;
      break;
    }
  }
}

if (isPrime) {
  document.querySelector('#target').textContent = `${num} is a prime number.`;
} else {
  document.querySelector('#target').textContent = `${num} is not a prime number.`;
}
