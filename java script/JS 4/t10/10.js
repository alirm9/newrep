'use strict';

const form = document.querySelector('#source');
const target = document.querySelector('#target');

form.addEventListener('submit', (evt) => {
  evt.preventDefault();
  const firstName = document.querySelector('input[name="firstname"]').value;
  const lastName = document.querySelector('input[name="lastname"]').value;
  target.textContent = `Your name is ${firstName} ${lastName}`;
});
