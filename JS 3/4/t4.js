'use strict';

const numbers = [];

while (true) {
  const input = Number(prompt('Enter a number (0 to stop):'));
  if (input === 0) {
    break;
  }
  numbers.push(input);
}

numbers.sort((a, b) => b - a);

for (const num of numbers) {
  console.log(num);
}