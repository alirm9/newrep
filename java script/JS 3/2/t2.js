'use strict';

const count = Number(prompt('Enter the number of participants:'));
const participants = [];

for (let i = 0; i < count; i++) {
  const name = prompt(`Enter name for participant ${i + 1}:`);
  participants.push(name);
}

participants.sort();

const ol = document.createElement('ol');
for (const name of participants) {
  const li = document.createElement('li');
  li.textContent = name;
  ol.appendChild(li);
}

document.querySelector('#target').appendChild(ol);