// write your custom js here
function fade_alerts() {
	var m = document.getElementsByClassName("alert");  // Return an array

    setTimeout(function(){
       if (m && m.length) {
           // m[0].classList.add('hide');
          m[0].style.display = "none";
       }
    }, 5000);

}

// call fade out after DOMContentLoaded
window.addEventListener('DOMContentLoaded', (event) => {
    fade_alerts();
});