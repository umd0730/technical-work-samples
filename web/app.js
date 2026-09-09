'use strict';
const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
function closeMenu(restoreFocus = false) {
  nav.classList.remove('open');
  menu.setAttribute('aria-expanded', 'false');
  if (restoreFocus) menu.focus();
}
menu.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(open));
  nav.classList.toggle('open', open);
});
nav.addEventListener('click', (event) => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') closeMenu(true);
});
window.matchMedia('(min-width: 621px)').addEventListener('change', () => closeMenu());
document.querySelector('form').addEventListener('submit', (event) => {
  event.preventDefault();
  const name = document.querySelector('#name');
  const message = document.querySelector('#message');
  for (const input of [name, message]) {
    input.setCustomValidity(input.value.trim() ? '' : 'Please enter more than spaces.');
  }
  if (!event.currentTarget.reportValidity()) return;
  document.querySelector('#form-status').textContent = `Preview ready for ${name.value.trim()}. Nothing was sent or saved.`;
});
for (const input of document.querySelectorAll('input, textarea')) {
  input.addEventListener('input', () => {
    input.setCustomValidity('');
    document.querySelector('#form-status').textContent = '';
  });
}
