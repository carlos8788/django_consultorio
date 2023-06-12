
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', cargar_datos, name='turnos'),
    path('mostrar_turnos', turnos, name='mostrar_turnos'),
    path('filtrar_fecha/', filtrar_fecha, name='filtrar_fecha'),
    path('paciente/', paciente, name='paciente'),
    path('diagnostico/<int:id>', diagnostico, name='diagnostico'),
    path('paciente/diagnostico/<int:id>', diagnostico, name='diagnostico'),
]
