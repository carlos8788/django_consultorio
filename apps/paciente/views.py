from django.shortcuts import render
from .models import Paciente, Fecha, Turno
from datetime import date, datetime
from django.shortcuts import render, redirect
from .forms import PacienteForm
from .tests import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

def format_data(data):
    pacientes_list = []
    for turno in data:
        # print(turno, 'turno')
        paciente_db = Paciente.objects.get(id=turno['paciente_id']).get_paciente()
        hora = Hora.objects.get(id=turno['hora_id'])
        fecha = Fecha.objects.get(id=turno['fecha_id'])
        paciente_db['hora'] = hora
        paciente_db['fecha'] = format_fecha(str(fecha))
        paciente_db['diagnostico'] = turno['diagnostico']
        paciente_db['id_turno'] = turno['id']
        
        pacientes_list.append(paciente_db)
         
    return pacientes_list

def format_fecha(data_fecha):
    fecha_recibida = data_fecha.split('-')
    return f'{fecha_recibida[2]}-{fecha_recibida[1]}-{fecha_recibida[0][2:]}'


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

@login_required
def turnos(request):
    # filtro = date(2023, 5, 18)
    turnos = Turno.objects.all().values()
    # print(turnos)
    pacientes = format_data(turnos)

    fechas = Fecha.objects.all()

    return render(request,'pages/mostrar_turnos.html', {'pacientes': pacientes, 'fechas': fechas})

@login_required
def filtrar_fecha(request):

    fecha_busqueda = request.GET.get('fecha_busqueda')

    fecha_busqueda = datetime.strptime(fecha_busqueda, "%Y-%m-%d").date()

    fecha = Fecha.objects.get(fecha=fecha_busqueda)
    turnos = Turno.objects.filter(fecha=fecha).values()
    pacientes = format_data(turnos)
    fechas = Fecha.objects.all()

    return render(request,'pages/mostrar_turnos.html', {'pacientes': pacientes, 'fechas': fechas})

@login_required
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
        
        turnos = paciente.turnos_paciente.all()  # Accede a todos los turnos del paciente
        
        for i in turnos:
            i = str(i).split(',')
            turno_dict = {}
            turno_dict['nombre'] = i[0]
            turno_dict['fecha'] = format_fecha(i[1])
            turno_dict['hora'] = i[2]
            turno_dict['id_turno'] = i[3]
            turnos_list.append(turno_dict)
            
    except Paciente.DoesNotExist :
        paciente = None
    except ValueError:
        # Manejar el error específico de ValueError aquí
        paciente = None
    return render(request, 'pages/paciente.html',{'paciente':paciente,'turnos': turnos_list, 'dnis': dnis})


@login_required
def diagnostico(request, id):
    
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)

        turno = Turno.objects.get(id=id)
        turno.diagnostico = data['diagnostico']
        turno.save()

        return JsonResponse({'message': 'Diagnóstico recibido'}, status=200)
    else:
        turno = Turno.objects.get(id=int(id)).get_id_diag_pac()
        paciente = Paciente.objects.get(id=turno['paciente']).get_paciente()
        # print(turno, 'TURNO_ID')
        # print(paciente)
        json_turno = {
            'id':turno['id'],
            'nombre': paciente['nombre'],
            'apellido': paciente['apellido'],
            'obra_social': str(paciente['obra_social']),
            'dni': paciente['dni'],
            'observaciones': paciente['observaciones'],
            'diagnostico': turno['diagnostico']
        }
        # return redirect('mostrar_turnos')
        return JsonResponse({'turno': json_turno}, status=200)
    

