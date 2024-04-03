const myDiv = document.getElementById('update_header')
const header = document.getElementsByTagName('header')[0]

myDiv.addEventListener('click', function() {
    header.textContent = 'New Header!!!'
})
