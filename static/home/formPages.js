document.addEventListener('DOMContentLoaded', function() {
  const generalForm = document.querySelector('.generalButton');
  formPages(generalForm, 'general')
})

function formPages(element, formToShow) {
  // get the nav button color
  const elms = document.querySelectorAll('#formNav');
  for (let elm of elms) {
    elm.classList.remove('w3-theme-d1')
  }
  element.classList.add('w3-theme-d1')

  // show the correct form
  const forms = document.querySelectorAll('.forms');
  for (let form of forms) {
    form.style.display = 'none';
    if (form.id === formToShow) {
      form.style.display = 'block';
    }
  }
}

// Show preview profile picture
imgInp.onchange = evt => {
  const [file] = imgInp.files
  if (file) {
    preview.src = URL.createObjectURL(file)
  }
  preview.style.display = 'block'
}