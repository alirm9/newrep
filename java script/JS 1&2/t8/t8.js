'use strict';

const startYear = Number(prompt('Enter start year:'));
const endYear = Number(prompt('Enter end year:'));

const ul = document.createElement('ul');

for (let year = startYear; year <= endYear; year++) {
  if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
    const li = document.createElement('li');
    li.textContent = year;
    ul.appendChild(li);
  }
}

document.querySelector('#target').appendChild(ul);
