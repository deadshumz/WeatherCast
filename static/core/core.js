console.log('JS loaded!')

favorite_star = document.getElementById('favorite-star')
favorite_btn = document.getElementById('favorite-btn')

function change_favorite(e, cityname) {
    const formData = new FormData(),
          xhr = new XMLHttpRequest(),
          localHref = window.location.href,
          csrfmiddlewaretoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    formData.append('favorite_change', cityname)

    xhr.open("POST", localHref);
    xhr.setRequestHeader('X-CSRFToken', csrfmiddlewaretoken);
    xhr.send(formData);

    class_list = ['text-warning', 'bi-star', 'bi-star-fill']
    class_list.map(el => e.firstChild.classList.toggle(el))
};
