'use strict';

const numDice = Number(prompt('Enter the number of dice:'));
const targetSum = Number(prompt('Enter the sum of eye numbers of interest:'));

const simulations = 10000;
let hits = 0;

for (let i = 0; i < simulations; i++) {
  let currentSum = 0;
  for (let d = 0; d < numDice; d++) {
    currentSum += Math.floor(Math.random() * 6) + 1;
  }
  if (currentSum === targetSum) {
    hits++;
  }
}

const probability = ((hits / simulations) * 100).toFixed(2);
document.querySelector('#target').textContent = `Probability to get sum ${targetSum} with ${numDice} dice is ${probability}%`;
