async function sendResultsToDoctor(test_id, doctor_username) {
  // get the button
  const button = document.getElementById(`${doctor_username}`);

  // make the fetch call
  if (button.innerText === 'Send') {
    // fetch to send
    const x = await fetch('/test_neo/send_results/', {
      method: 'POST',
      body: JSON.stringify({
        test_id: test_id,
        doctor_username: doctor_username,
        send: true
      })
    })
  } else {
    // fetch to unsend
    const x = await fetch('/test_neo/send_results/', {
      method: 'POST',
      body: JSON.stringify({
        test_id: test_id,
        doctor_username: doctor_username,
        send: false
      })
    })
  }

  // change button
  if (button.innerText === 'Send') {
    button.innerText = 'Unsend';
  } else {
    button.innerText = 'Send';
  }
}