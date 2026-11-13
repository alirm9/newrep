'use strict';

function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

const ul = document.createElement('ul');
let roll = 0;

while (roll !== 6) {
  roll = rollDice();
  const li = document.createElement('li');
  li.textContent = roll;
  ul.appendChild(li);
}

document.querySelector('#target').appendChild(ul);