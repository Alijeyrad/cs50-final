async function sendResultsToDoctor(test_id, doctor_username) {
  // get the button
  const button = document.getElementById(`${doctor_username}${test_id}`);

  // make the fetch call
  if (button.innerHTML === 'Send') {
    // fetch to send
    button.innerHTML = `<p style="margin:0 7px;"><i class="fa fa-spinner w3-spin" style="font-size:20px"></i></p>`;
    const x = await fetch('/test_neo/send_results/', {
      method: 'POST',
      body: JSON.stringify({
        test_id: test_id,
        doctor_username: doctor_username,
        send: true
      })
    })

    button.innerText = 'Unsend';

  } else {
    // fetch to unsend
    button.innerHTML = `<p style="margin:0 7px;"><i class="fa fa-spinner w3-spin" style="font-size:20px"></i></p>`;
    const x = await fetch('/test_neo/send_results/', {
      method: 'POST',
      body: JSON.stringify({
        test_id: test_id,
        doctor_username: doctor_username,
        send: false
      })
    })

    button.innerText = 'Send';

  }

  // change button
  // if (button.innerText === 'Send') {
  //   button.innerText = 'Unsend';
  // } else {
  //   button.innerText = 'Send';
  // }
}