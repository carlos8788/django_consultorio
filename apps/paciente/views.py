from django.shortcuts import render
from .models import Paciente, Fecha, Turno
from datetime import date, datetime
from django.shortcuts import render, redirect
from .forms import PacienteForm
from .tests import *
from django.contrib.auth.decorators import login_required

def cargar_datos(request):
    # datos()
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['obra_social'] is None:
               obra_social_m =  form.cleaned_data['nueva_obra_social']
            else:
               obra_social_m =  form.cleaned_data['obra_social']

            paciente = Paciente(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                dni=form.cleaned_data['dni'],
                celular=form.cleaned_data['celular'],
                obra_social=obra_social_m,
                observaciones=form.cleaned_data['observaciones'],
                fecha = form.cleaned_data['fecha'],
                hora = form.cleaned_data['hora']
            )
            paciente.save() # Guarda los datos en la base de datos
            return redirect('home')
    else:
        form = PacienteForm()

    return render(request, 'pages/turnos.html', {'form': form})



# Create your views here.
@login_required
def turnos(request):
    # filtro = date(2023, 5, 18)
    turnos = Turno.objects.all().values()
    pacientes = []
    for turno in turnos:
        # print(turno)
        paciente = Paciente.objects.get(id=turno['paciente_id']).get_paciente()
        hora = Hora.objects.get(id=turno['hora_id'])
        fecha = Fecha.objects.get(id=turno['fecha_id'])
        paciente['hora'] = hora
        paciente['fecha'] = fecha
        paciente['id_turno'] = turno['id']
        # print(paciente)
        pacientes.append(paciente)
         # print(turno.paciente, turno.fecha, turno.hora, turno.diagnostico)

    fechas = Fecha.objects.all()
    # print(pacientes)
    return render(request,'pages/mostrar_turnos.html', {'pacientes': pacientes, 'fechas': fechas})

@login_required
def filtrar_fecha(request):
    # Obtener la fecha de la solicitud
    fecha_busqueda = request.GET.get('fecha_busqueda')
    print(fecha_busqueda)
    # Convertir la cadena de fecha en un objeto datetime.date
    fecha_busqueda = datetime.strptime(fecha_busqueda, "%Y-%m-%d").date()
    # Filtrar los pacientes por la fecha
    pacientes = Paciente.objects.filter(fecha__fecha=fecha_busqueda)
    fechas = Fecha.objects.all()
    # Renderizar una plantilla con los pacientes filtrados
    print(fechas)
    return render(request,'pages/mostrar_turnos.html', {'pacientes': pacientes, 'fechas': fechas})

def paciente(request):
    if request.method == 'POST':
        pass
    dni_input = request.GET.get('dni_input', 'dni_input')
    dni_select = request.GET.get('dni_select', 'dni_select')
    dnis = Paciente.objects.values_list('dni', flat=True)
    turnos_list = []
    
    try:
        if dni_input:
            paciente = Paciente.objects.get(dni=dni_input)
        else:
            paciente = Paciente.objects.get(dni=dni_select)
        print(paciente)
        turnos = paciente.turnos_paciente.all()  # Accede a todos los turnos del paciente

        for i in turnos:
            i = str(i).split(',')
            turno_dict = {}
            turno_dict['nombre'] = i[0]
            turno_dict['fecha'] = i[1]
            turno_dict['hora'] = i[2]
            turnos_list.append(turno_dict)
            
    except Paciente.DoesNotExist :
        paciente = None
    except ValueError:
        # Manejar el error específico de ValueError aquí
        paciente = None
    return render(request, 'pages/paciente.html',{'paciente':paciente,'turnos': turnos_list, 'dnis': dnis})