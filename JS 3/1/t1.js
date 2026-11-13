'use strict';

const numbers = [];

for (let i = 0; i < 5; i++) {
  const num = Number(prompt(`Enter number ${i + 1} of 5:`));
  numbers.push(num);
}

for (let i = numbers.length - 1; i >= 0; i--) {
  console.log(numbers[i]);
}