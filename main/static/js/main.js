// Smooth scroll for anchor links
(function(){
  document.addEventListener('click', function(e){
    const target = e.target.closest('a');
    if(!target) return;
    const href = target.getAttribute('href');
    if(!href || href.charAt(0) !== '#') return;
    const el = document.querySelector(href);
    if(!el) return;
    e.preventDefault();
    el.scrollIntoView({behavior:'smooth'});
  });
  // simple sticky header shadow toggle
  const header = document.querySelector('.site-header');
  if(header){
    window.addEventListener('scroll', function(){
      if(window.scrollY > 10){
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }
})();
