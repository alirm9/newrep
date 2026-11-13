'use strict';

const studentName = prompt("Enter the student's name:");
const draw = Math.floor(Math.random() * 4) + 1;
let house = '';

if (draw === 1) {
  house = 'Gryffindor';
} else if (draw === 2) {
  house = 'Slytherin';
} else if (draw === 3) {
  house = 'Hufflepuff';
} else {
  house = 'Ravenclaw';
}

document.querySelector('#target').textContent = `${studentName}, you are ${house}.`;
