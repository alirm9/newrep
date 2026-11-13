'use strict';

const calcInput = document.querySelector('#calculation');
const startBtn = document.querySelector('#start');
const resultP = document.querySelector('#result');

startBtn.addEventListener('click', () => {
  const expr = calcInput.value.trim();
  let answer;

  if (expr.includes('+')) {
    const [a, b] = expr.split('+').map(Number);
    answer = a + b;
  } else if (expr.includes('-')) {
    const [a, b] = expr.split('-').map(Number);
    answer = a - b;
  } else if (expr.includes('*')) {
    const [a, b] = expr.split('*').map(Number);
    answer = a * b;
  } else if (expr.includes('/')) {
    const [a, b] = expr.split('/').map(Number);
    answer = b !== 0 ? Math.floor(a / b) : 'Cannot divide by zero';
  } else {
    answer = 'Invalid expression';
  }

  resultP.textContent = answer;
});
