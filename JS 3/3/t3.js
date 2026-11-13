'use strict';

const dogs = [];

for (let i = 0; i < 6; i++) {
  const dogName = prompt(`Enter name for dog ${i + 1}:`);
  dogs.push(dogName);
}

dogs.sort().reverse();

const ul = document.createElement('ul');
for (const dog of dogs) {
  const li = document.createElement('li');
  li.textContent = dog;
  ul.appendChild(li);
}

document.querySelector('#target').appendChild(ul);