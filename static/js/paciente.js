const nuevoTurno = document.getElementById('nuevoTurno');
const modalNuevoTurno = new bootstrap.Modal(document.getElementById('modalNuevoTurno'));
nuevoTurno.addEventListener('click', () => {
    modalNuevoTurno.show();
});

const confirmarTurno = document.getElementById('confirmarTurno');

confirmarTurno.addEventListener('submit', (event) => {
    event.preventDefault();
    const paciente = event.target.querySelector('input[name="paciente"]').value;
    const user = Object.fromEntries(new FormData(event.target))
    
    const SolicitarTurno = {
        paciente,
        fecha: user.fecha,
        hora: user.horario,
        diagnostico: user.comentario
    }

    console.log(SolicitarTurno);

})