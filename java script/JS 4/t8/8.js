'use strict';

const num1Input = document.querySelector('#num1');
const num2Input = document.querySelector('#num2');
const operationSelect = document.querySelector('#operation');
const startBtn = document.querySelector('#start');
const resultP = document.querySelector('#result');

startBtn.addEventListener('click', () => {
  const n1 = Number(num1Input.value);
  const n2 = Number(num2Input.value);
  const op = operationSelect.value;
  let answer;

  if (op === 'add') {
    answer = n1 + n2;
  } else if (op === 'sub') {
    answer = n1 - n2;
  } else if (op === 'multi') {
    answer = n1 * n2;
  } else if (op === 'div') {
    answer = n2 !== 0 ? n1 / n2 : 'Cannot divide by zero';
  }

  resultP.textContent = answer;
});
