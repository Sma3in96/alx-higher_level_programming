const div = document.getElementById('character')

fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
.then(Response => {
    if (!Response.ok) {
        throw new console.error("no response");
    }
    return Response.json();
})
.then(data => {
    const obj = data
    div.textContent = obj.name
})
.catch(error => {
    console.error(error)
})


