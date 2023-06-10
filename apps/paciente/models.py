from django.db import models
from datetime import time, timedelta, datetime
from apps.obra_sociales.models import ObraSocial
# from datetimewidget.widgets import DateTimeWidget
# Create your models here.
class Fecha(models.Model):
    fecha = models.DateField()

    def __str__(self):
        return str(self.fecha)

class Hora(models.Model):
    hora_choices = []
    hora_inicio = datetime.strptime('16:00', '%H:%M').time()  # Hora de inicio: 16:30
    hora_fin = datetime.strptime('19:00', '%H:%M').time()  # Hora de fin: 19:00
    incremento = timedelta(minutes=10)  # Incremento de 10 minutos

    hora_actual = datetime.combine(datetime.today(), hora_inicio)

    while hora_actual.time() <= hora_fin:
        hora_choices.append((hora_actual.strftime('%H:%M'), hora_actual.strftime('%I:%M')))
        hora_actual += incremento

    hora = models.CharField(max_length=10, choices=hora_choices)

    def __str__(self):
        return str(self.hora)[0:-3]

class Paciente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=90)
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.DO_NOTHING)
    celular = models.CharField(max_length=12)
    dni = models.IntegerField()
    observaciones = models.TextField(blank=True)
    nombre_completo = models.CharField(max_length=200, editable=False, default='')

    def save(self, *args, **kwargs):
        self.nombre_completo = f'{self.nombre} {self.apellido}'
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    
    def get_paciente(self):
        return {
            'nombre':self.nombre,
            'apellido':self.apellido,
            'obra_social':self.obra_social,
            'celular':self.celular,
            'dni':self.dni,
            'observaciones':self.observaciones
        }
    

class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='turnos_paciente')
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE, related_name='turnos_fecha')
    hora = models.ForeignKey(Hora, on_delete=models.CASCADE, blank=False, related_name='turnos_hora')
    diagnostico = models.TextField(blank=True, default='')
    def __str__(self):
        simp_hora = str(self.hora.hora)[0:-3]
        return f'{self.paciente.nombre} {self.paciente.apellido},{self.fecha.fecha},{simp_hora}'