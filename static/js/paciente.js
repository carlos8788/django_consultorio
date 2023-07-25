const nuevoTurno = document.getElementById('nuevoTurno');
const modalNuevoTurno = new bootstrap.Modal(document.getElementById('modalNuevoTurno'));
nuevoTurno.addEventListener('click', () => {
    modalNuevoTurno.show();
});