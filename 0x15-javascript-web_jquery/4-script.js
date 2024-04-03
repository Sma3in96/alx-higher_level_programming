const header = document.getElementsByTagName('header')
const div = document.getElementById('toggle_header')

div.addEventListener('click', function() {
    if (header[0].classList.contains('green')) {
        header[0].classList.remove('green')
        header[0].classList.add('red')
    } else if (header[0].classList.contains('red')) {
        header[0].classList.remove('red')
        header[0].classList.add('green')
    }
})
