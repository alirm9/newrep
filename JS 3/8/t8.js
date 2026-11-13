'use strict';

function concat(strings) {
  let result = '';
  for (const str of strings) {
    result += str;
  }
  return result;
}

const names = ['Johnny', 'DeeDee', 'Joey', 'Marky'];
const combined = concat(names);

document.querySelector('#target').textContent = combined;