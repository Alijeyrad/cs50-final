function myFunction(id) {
  var x = document.getElementById(id);
  
  if (x.className.indexOf("w3-show") == -1) {
    // get the other one and close it
    // before opening this one
    for (let button of document.getElementsByClassName('btns')) {
      button.classList.remove('w3-show');
    }
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}