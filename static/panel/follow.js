async function follow(follower, followee) {
  var followButton = document.getElementById('followButton');
  var followText = document.getElementById('followText');
  var count = document.querySelector('#followerCount').innerHTML;
  
  // make the fetch call
  if (followText.innerHTML == 'Follow') {
    // fetch to follow
    const x = await fetch('/panel/follow_api', {
      method: 'POST',
      body: JSON.stringify({
        follower: follower,
        followee: followee,
        follow: true
      })
    })

    // change followers count
    document.querySelector('#followerCount').innerHTML = parseInt(count) + 1;
    
  } else {
    // fetch to unfollow
    const x = await fetch('/panel/follow_api', {
      method: 'POST',
      body: JSON.stringify({
        follower: follower,
        followee: followee,
        follow: false
      })
    })

    // change followers count
    document.getElementById('followerCount').innerHTML = parseInt(count) - 1;
  }

  // change the button
  if (followText.innerText === 'Unfollow') {
    followText.innerText = 'Follow';
  } else {
    followText.innerText = 'Unfollow'
  }
}