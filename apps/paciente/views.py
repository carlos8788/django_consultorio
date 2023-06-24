from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q

from .models import Paciente, Fecha, Turno, Hora
from .forms import PacienteForm

from datetime import datetime
import os
import json
import traceback

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
    try:
        turnos = Turno.objects.all().values()
        pacientes = format_data(turnos)
        fechas = Fecha.objects.all()

        return render(request,'pages/mostrar_turnos.html', {'pacientes': pacientes, 'fechas': fechas})
    except Exception as e:
        error_message = traceback.format_exc()
        return JsonResponse({'error':error_message}, status=500)

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
def paciente(request, dni=None):
    
    dni_input = request.GET.get('dni_input', 'dni_input')
    dni_select = request.GET.get('dni_select', 'dni_select')
    dnis = Paciente.objects.values_list('dni', flat=True)
    turnos_list = []
    
    try:
        if dni:
            paciente = Paciente.objects.get(dni=int(dni))
        elif dni_input:
            paciente = Paciente.objects.get(dni=dni_input)
            print(paciente)
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
    # print(paciente.get_paciente())
    return render(request, 'pages/paciente.html',{'paciente':paciente,'turnos': turnos_list, 'dnis': dnis})

@login_required
@require_POST
def update_paciente(request, dni):
    # Obtén los datos de las observaciones desde la solicitud
    observaciones = request.POST.get('observaciones')

    # Encuentra el paciente correspondiente en la base de datos
    paciente = Paciente.objects.get(dni=dni)
    print(paciente)
    # Actualiza las observaciones
    paciente.observaciones = observaciones
    print(paciente.observaciones)
    paciente.save()

    # Devuelve una respuesta
    return redirect(f'/turnos/paciente/dni={dni}')


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
    
@login_required
def all_pacientes(request):
    numero_pagina = request.GET.get('page', 1)

    pacientes = Paciente.objects.all()
    pacientes = [p.get_paciente() for p in pacientes]

    paginator = Paginator(pacientes, 20)

    try:
        pagina_actual = paginator.page(numero_pagina)
    except EmptyPage:
        pagina_actual = paginator.page(1)  # Si el número de página está fuera de rango, muestra la primera página

    return render(request, 'pages/pacientes.html', {'pagina': pagina_actual})

def is_allowed_url(request):
    allowed_url = os.environ.get('URL')
    allowed_url += '/dar_turno'  # Reemplaza con la URL permitida
    print(allowed_url)
    return request.path == allowed_url


# @user_passes_test(is_allowed_url)
@login_required
def dar_turnos(request):
    pacientes = Paciente.objects.all()
    pacientes = [p.get_paciente() for p in pacientes]
    def serializer_obra_social(paciente):
        paciente['obra_social'] = paciente['obra_social'].to_json()
        return paciente
    pacientes = [serializer_obra_social(pac) for pac in pacientes]
    
    return JsonResponse({'pacientes': pacientes}, status=200)
@login_required
def page_buscar_paciente(request):
    return render(request, 'pages/buscar_paciente.html')

@login_required
def buscar_paciente_nombre(request, cadena):
    print(cadena)
    print(Paciente.objects.filter(Q(nombre__icontains=cadena)))
    pacientes = list(Paciente.objects.filter(Q(nombre__icontains=cadena)).values())
    print(pacientes)
    if not pacientes:
        return JsonResponse({'error': 'No se encontraron pacientes'}, status=404)
    return JsonResponse(pacientes, safe=False)