const btnClose = document.getElementById('close');
const btnSave = document.getElementById('save');
const bodyTable = document.getElementById('body_table')
const modalTitle = document.getElementById('modalTitle');
const dataPaciente = document.getElementById('dataPaciente');
const diagnostico = document.getElementById('diagnostico');
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const btnCloseFunction = (mod) => {
    mod.classList.remove("show");
    mod.style.display = "none";
    mod.removeAttribute("aria-modal");
    mod.setAttribute("aria-hidden", 'true');
    diagnostico.value = ''
};


let urlPost = ''
let modal;
Array.from(bodyTable.children).forEach(element => {
    Array.from(element.children).forEach(element_2 => {

        if (element_2.children.length > 0) {
            element_2.children.item(0).addEventListener('click', (e) => {

                e.preventDefault();
                let url = `diagnostico/${element_2.children.item(0).id.trim()}`
                urlPost = url

                fetch(url, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    }
                })
                    .then(response => response.json())
                    .then(data => {
                        modalTitle.textContent = `${data.turno.nombre} ${data.turno.apellido}`
                        dataPaciente.innerHTML = `<strong>DNI:</strong> ${data.turno.dni} 
                                                <strong>O. Social:</strong> ${data.turno.obra_social}`
                        diagnostico.value = data.turno.diagnostico
                    }).catch((error) => console.log(error));

                const targetModal = element_2.children.item(0).getAttribute("data-target");
                modal = document.querySelector(targetModal);
                if (modal) {
                    modal.classList.add("show");
                    modal.style.display = "block";
                    modal.setAttribute("aria-modal", "true");
                    modal.removeAttribute("aria-hidden");

                    btnClose.addEventListener('click', () => btnCloseFunction(modal))
                }
            });

        }
    });
});


btnSave.addEventListener('click', () => {

    fetch(urlPost, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },

        body: JSON.stringify({ diagnostico: diagnostico.value }),

    })
        .then(response => response.json())
        .then(data => {
            alert(data.message)
        })
        .catch(error => {
            console.log(error)
        });

    btnCloseFunction(modal)
    diagnostico.value = ''
});
