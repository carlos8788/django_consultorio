from django.contrib import admin
from .models import Paciente, Fecha, Hora
# Register your models here.
admin.site.register(Paciente)
admin.site.register(Fecha)
admin.site.register(Hora)