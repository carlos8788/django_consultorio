let input = document.getElementById('inputPaciente');
let resultados = document.getElementById('body_table');
let sinResultados = document.getElementById('sinResultados');
let btnCel = document.getElementById('btnCel');
console.log(sinResultados);
const filterInfo = (datos) => {
    let pacientes ='';
        

        let filtrados = datos.filter(paciente => paciente.nombre.toLowerCase().includes(input.value.toLowerCase()));
        console.log(filtrados.length);
        if(filtrados.length === 0)  {
            sinResultados.innerHTML = `<h1 class="text-center mb-5">Paciente no encontrado</h1>`
            resultados.innerHTML = ''
        }
            
        filtrados.forEach((paciente, index) => {

            pacientes += `
                            <tr>
                                <td class="">${index + 1}</td>
                                <td class="text-center"><a href="/turnos/paciente/dni=${paciente.dni}">${paciente.nombre} ${paciente.apellido}</a></td><td class="text-center">${paciente.dni}</td>
                                <td class="text-center">${paciente.obra_social.nombre}</td>
                                <td class="text-center">${paciente.celular}</td>
                            </tr>
                         `
        });
        resultados.innerHTML = pacientes
}

async function obtenerDatos() {
    const response = await fetch('http://localhost:8000/turnos/pacientes/api/dar_turno');
    const datos = await response.json();
    return datos.pacientes; 
}

async function main() {
    const datos = await obtenerDatos();
    
    input.addEventListener('input', function () {
        // Limpia los resultados anteriores
        filterInfo(datos);
        
    });
    
    
}

main();

