'use strict';

const rollsCount = Number(prompt('Enter the number of dice rolls:'));
let sum = 0;

for (let i = 0; i < rollsCount; i++) {
  const roll = Math.floor(Math.random() * 6) + 1;
  sum += roll;
}

document.querySelector('#target').textContent = `Sum of ${rollsCount} dice rolls: ${sum}`;
