document.addEventListener("DOMContentLoaded", async function() {
  const doctor_username = document.getElementById('username').innerHTML;

  const x = await fetch('/panel/rate' + '?' + `doctor=${doctor_username}`)
  const response = await x.json();
  if (response.rate) {
    rate(response.rate)
  }
});

function clearRates() {
  let i = 1;
  do {
    document.querySelector(`#rate${i}`).classList.remove('checked');
    i += 1;
  } while (i < 6);
}

function rate(rate, doctor = null) {
  clearRates();
  let i = 1;
  do {
    document.querySelector(`#rate${i}`).classList.add('checked');
    i += 1
  } while (i <= rate)

  // send rating to server
  if (doctor !== null) {
    const x = fetch('/panel/rate', {
      method: 'POST',
      body: JSON.stringify({
        doctor: doctor,
        rate: rate
      })
    })
  }
}