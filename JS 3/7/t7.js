'use strict';

function rollDice(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

const maxSides = Number(prompt('Enter the number of sides on the dice:'));
const ul = document.createElement('ul');
let roll = 0;

while (roll !== maxSides) {
  roll = rollDice(maxSides);
  const li = document.createElement('li');
  li.textContent = roll;
  ul.appendChild(li);
}

document.querySelector('#target').appendChild(ul);