const classUser = document.getElementById('id_username')
classUser.classList.add('form-control')


const classPassword = document.getElementById('id_password')
classPassword.classList.add('form-control')


const label = document.querySelectorAll('label')
console.log(label);

Array.from(label).forEach((element) => {
    element.id = `${element.htmlFor}_label`
    element.classList.add('form-label')

});

const labelUser = document.getElementById('id_username_label')
const passwordUser = document.getElementById('id_password_label')

classUser.addEventListener('focus', function () {
    labelUser.classList.add('text-info');
});

// Evento cuando el input pierde el foco
classUser.addEventListener('blur', function () {
    labelUser.classList.remove('text-info');
});

classPassword.addEventListener('focus', function () {
    passwordUser.classList.add('text-info');
});

// Evento cuando el input pierde el foco
classPassword.addEventListener('blur', function () {
    passwordUser.classList.remove('text-info');
});