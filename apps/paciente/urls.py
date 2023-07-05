
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', cargar_datos, name='turnos'),
    path('mostrar_turnos', turnos, name='mostrar_turnos'),
    path('filtrar_fecha/', filtrar_fecha, name='filtrar_fecha'),
    path('paciente/', paciente, name='paciente'),
    path('paciente/dni=<str:dni>', paciente, name='paciente_dni_select'),
    path('pacientes/', all_pacientes, name='pacientes'),
    path('diagnostico/<int:id>', diagnostico, name='diagnostico'),
    path('paciente/diagnostico/<int:id>', diagnostico, name='diagnostico'),
    path('pacientes/dar_turno', page_buscar_paciente, name='buscar_paciente'),
    path('pacientes/api/obtener_turno', obtener_turno),
    path('pacientes/dar_turno/buscar_paciente/<str:cadena>', buscar_paciente_nombre, name='buscar_paciente'),
    path('pacientes/api/actualizar_obs/<str:dni>', update_paciente, name='update_obs'),
    path('pacientes/api/dar_turno', update_paciente, name='dar_turno'),
]
# http://localhost:8000/turnos/pacientes/dar_turno