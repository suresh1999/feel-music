$( document ).ready(function(){
  $(".button-collapse").sideNav();
  // $("#preloader").show();
})
//preloader
        var overlay = document.getElementById("overlay");

        window.addEventListener('load', function(){
          overlay.style.display = 'none';
        })


//scrollanimation
window.sr = ScrollReveal();
sr.reveal('.contents');
// sr.reveal('.row');
sr.reveal('.container');
