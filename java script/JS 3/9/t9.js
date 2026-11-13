'use strict';

function even(numbers) {
  const evenNumbers = [];
  for (const num of numbers) {
    if (num % 2 === 0) {
      evenNumbers.push(num);
    }
  }
  return evenNumbers;
}

const originalArray = [2, 7, 4, 9, 12, 15, 8];
const filteredArray = even(originalArray);

console.log('Original array:', originalArray);
console.log('Even numbers array:', filteredArray);