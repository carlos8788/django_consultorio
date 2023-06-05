from django.shortcuts import render
from .models import Paciente, Fecha, Hora
from datetime import date, datetime
from django.shortcuts import render, redirect
from .forms import PacienteForm
from .tests import *
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
def turnos(request):
    # filtro = date(2023, 5, 18)
    pacientes = Paciente.objects.all()
    fechas = Fecha.objects.all()
    # print(pacientes)
    return render(request,'pages/mostrar_turnos.html', {'pacientes': pacientes, 'fechas': fechas})

def filtrar_fecha(request):
    # Obtener la fecha de la solicitud
    fecha_busqueda = request.GET.get('fecha_busqueda')
    # Convertir la cadena de fecha en un objeto datetime.date
    fecha_busqueda = datetime.strptime(fecha_busqueda, "%Y-%m-%d").date()
    # Filtrar los pacientes por la fecha
    pacientes = Paciente.objects.filter(fecha__fecha=fecha_busqueda)
    fechas = Fecha.objects.all()
    # Renderizar una plantilla con los pacientes filtrados
    return render(request,'pages/mostrar_turnos.html', {'pacientes': pacientes, 'fechas': fechas})