document.addEventListener('DOMContentLoaded', function() {
    const myDiv = document.getElementById('hello')

    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(Response => {
        if (!Response.ok) {
            console.error ("network")
        }
        return Response.json()
    })
    .then(data => {
        myDiv.textContent = data.hello
    })
    .catch(error => {
        console.error(error)
    })
})
