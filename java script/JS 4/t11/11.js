'use strict';

const picArray = [
  {
    title: 'Title 1',
    caption: 'Caption 1',
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sodales enim eget leo condimentum vulputate. Sed lacinia consectetur fermentum. Vestibulum lobortis purus id nisi mattis posuere. Praesent sagittis justo quis nibh ullamcorper, eget elementum lorem consectetur. Pellentesque eu consequat justo, eu sodales eros.',
    image: {
      large: 'img/pic1.jpg',
      medium: 'thumbnails/pic1.jpg',
    },
  },
  {
    title: 'Title 2',
    caption: 'Caption 2',
    description:
      'Donec dignissim tincidunt nisl, non scelerisque massa pharetra ut. Sed vel velit ante. Aenean quis viverra magna. Praesent eget cursus urna. Ut rhoncus interdum dolor non tincidunt. Sed vehicula consequat facilisis. Pellentesque pulvinar sem nisl, ac vestibulum erat rhoncus id. Vestibulum tincidunt sapien eu ipsum tincidunt pulvinar. ',
    image: {
      large: 'img/pic2.jpg',
      medium: 'thumbnails/pic2.jpg',
    },
  },
  {
    title: 'Title 3',
    caption: 'Caption 3',
    description:
      'Phasellus imperdiet nunc tincidunt molestie vestibulum. Donec dictum suscipit nibh. Sed vel velit ante. Aenean quis viverra magna. Praesent eget cursus urna. Ut rhoncus interdum dolor non tincidunt. Sed vehicula consequat facilisis. Pellentesque pulvinar sem nisl, ac vestibulum erat rhoncus id. ',
    image: {
      large: 'img/pic3.jpg',
      medium: 'thumbnails/pic3.jpg',
    },
  },
];

const section = document.querySelector('#pictures');
const dialog = document.querySelector('dialog');
const dialogImg = dialog.querySelector('img');
const closeBtn = dialog.querySelector('span');

for (const pic of picArray) {
  const article = document.createElement('article');
  article.classList.add('card');

  const h2 = document.createElement('h2');
  h2.textContent = pic.title;

  const figure = document.createElement('figure');
  const img = document.createElement('img');
  img.src = pic.image.medium;
  img.alt = pic.title;

  const figcaption = document.createElement('figcaption');
  figcaption.textContent = pic.caption;

  figure.appendChild(img);
  figure.appendChild(figcaption);

  const p = document.createElement('p');
  p.textContent = pic.description;

  article.appendChild(h2);
  article.appendChild(figure);
  article.appendChild(p);

  article.addEventListener('click', () => {
    dialogImg.src = pic.image.large;
    dialogImg.alt = pic.title;
    dialog.showModal();
  });

  section.appendChild(article);
}

closeBtn.addEventListener('click', () => {
  dialog.close();
});
