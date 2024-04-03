const header = document.getElementsByTagName('header')
const div = document.getElementById('red_header')

div.addEventListener('click', function() {
    header[0].style = 'color: #ff0000'
})
