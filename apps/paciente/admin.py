from django.contrib import admin
from .models import Paciente, Fecha, Hora, Turno
from django.utils.translation import gettext_lazy as _
from django.db.models import Value as V
from django.db.models.functions import Concat
# Register your models here.

class TurnoAdmin(admin.ModelAdmin):
    list_filter = ('paciente__nombre_completo','fecha')


admin.site.register(Turno, TurnoAdmin)
models = [Fecha, Hora, Paciente]
admin.site.register(models)
