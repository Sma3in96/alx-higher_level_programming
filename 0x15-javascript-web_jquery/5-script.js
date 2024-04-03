const ul = document.getElementsByClassName('my_list')[0]
const div = document.getElementById('add_item')


div.addEventListener('click', function() {
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
})
