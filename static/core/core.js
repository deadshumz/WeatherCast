console.log('JS loaded!')

favorite_star = document.getElementById('favorite-star')
favorite_btn = document.getElementById('favorite-btn')

function change_favorite(e, cityname) {

    let formData = new FormData();
    formData.append('favorite_change', cityname)

    let xhr = new XMLHttpRequest();
    xhr.open("POST", window.location.href);
    xhr.setRequestHeader('X-CSRFToken', document.querySelector('[name=csrfmiddlewaretoken]').value);
    xhr.send(formData);

    class_list = ['text-warning', 'bi-star', 'bi-star-fill']
    for(let i in class_list) {
        e.firstChild.classList.toggle(class_list[i])
    }
}