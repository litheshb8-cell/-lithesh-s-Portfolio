document.addEventListener('DOMContentLoaded', () => {

  /* ---------- Footer year ---------- */
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- Mobile menu toggle ---------- */
  const menuToggle = document.getElementById('menuToggle');
  const tabs = document.getElementById('tabs');
  if (menuToggle && tabs) {
    menuToggle.addEventListener('click', () => {
      tabs.classList.toggle('open');
    });
    tabs.querySelectorAll('.tab').forEach(tab => {
      tab.addEventListener('click', () => tabs.classList.remove('open'));
    });
  }

  /* ---------- Typing animation in hero ---------- */
  const typedEl = document.getElementById('typed');
  const phrases = [
    'I build websites.',
    'I write clean code.',
    'I solve problems.',
    'I keep learning.'
  ];
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (typedEl && !reduceMotion) {
    let phraseIndex = 0;
    let charIndex = 0;
    let deleting = false;

    function tick() {
      const current = phrases[phraseIndex];

      if (!deleting) {
        charIndex++;
        typedEl.textContent = current.slice(0, charIndex);
        if (charIndex === current.length) {
          deleting = true;
          setTimeout(tick, 1400);
          return;
        }
      } else {
        charIndex--;
        typedEl.textContent = current.slice(0, charIndex);
        if (charIndex === 0) {
          deleting = false;
          phraseIndex = (phraseIndex + 1) % phrases.length;
        }
      }
      setTimeout(tick, deleting ? 35 : 55);
    }
    tick();
  } else if (typedEl) {
    typedEl.textContent = phrases[0];
  }

  /* ---------- Active tab highlighting on scroll ---------- */
  const sections = document.querySelectorAll('main .section');
  const tabLinks = document.querySelectorAll('.tab');

  const setActiveTab = (id) => {
    tabLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
    });
  };

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      }
    });
  }, { threshold: 0.15 });

  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        setActiveTab(entry.target.id);
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });

  sections.forEach(section => {
    revealObserver.observe(section);
    navObserver.observe(section);
  });

  /* ---------- Contact form (front-end only placeholder) ---------- */
  const form = document.getElementById('contactForm');
  const status = document.getElementById('formStatus');

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = form.name.value.trim();
      if (!name) return;

      status.textContent = `Thanks, ${name.split(' ')[0]} — connect a backend or form service to send this for real.`;
      form.reset();

      setTimeout(() => { status.textContent = ''; }, 6000);
    });
  }

});
