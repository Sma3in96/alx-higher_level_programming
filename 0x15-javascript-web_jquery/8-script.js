const list = document.getElementById('list_movies')

fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
.then(Response => {
    if (!Response.ok) {
        console.error ("network")
    }
    return Response.json()
})
.then(data => {
    for (item in data.results) {
        const li = document.createElement('li')
        li.textContent = data.results[item].title
        list.appendChild(li)
    }
})
.catch(error => {
    console.error(error)
})
