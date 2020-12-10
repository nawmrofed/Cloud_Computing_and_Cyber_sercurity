const update = document.querySelector('#update-button')
const deleteButton = document.querySelector('#delete-button')
const messageDiv = document.querySelector('#message')

update.addEventListener('click', _ => {
    const name = document.getElementById("replace_name").value;
    const value = document.getElementById("replace_quote").value;
    fetch('/quotes', {
      method: 'put',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: name,
        quote: value
      })
    })
    .then(res => {
        if (res.ok) return res.json()
      })
    .then(response => {
        window.location.reload(true)
    })
  })

deleteButton.addEventListener('click', _ => {
    const name = document.getElementById("del_name").value;
fetch('/quotes', {
    method: 'delete',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
    name: name
    })
})
    .then(res => {
        if (res.ok) return res.json()
    })
    .then(response => {
        if (response === 'No quote to delete') {
          messageDiv.textContent = 'No Darth Vadar quote to delete'
        } else {
          window.location.reload()
        }
      })
      .catch(console.error)
})