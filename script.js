document.getElementById('contact-form').addEventListener('submit', function (e) {
  e.preventDefault();
  alert('Thank you for reaching out! I’ll get back to you soon.');
  document.getElementById('contact-form').reset();
});