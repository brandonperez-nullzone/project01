// script.js for frontend Hello World animation

document.addEventListener('DOMContentLoaded', function() {
  const message = document.getElementById('message');
  let visible = true;
  setInterval(function() {
    visible = !visible;
    message.style.opacity = visible ? 1 : 0;
  }, 950);
});
