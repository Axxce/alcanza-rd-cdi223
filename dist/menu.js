document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.menu-toggle');
  const drawer = document.querySelector('#site-drawer');
  const backdrop = document.querySelector('#drawer-backdrop');
  if (!toggle || !drawer || !backdrop) return;

  function setOpen(open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Cerrar menú de navegación' : 'Abrir menú de navegación');
    drawer.setAttribute('aria-hidden', String(!open));
    drawer.classList.toggle('is-open', open);
    backdrop.hidden = !open;
    backdrop.classList.toggle('is-open', open);
    document.body.classList.toggle('menu-open', open);
    if (open) drawer.querySelector('a[aria-current="page"]')?.focus();
    else toggle.focus();
  }

  toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  backdrop.addEventListener('click', () => setOpen(false));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') setOpen(false);
  });
});
