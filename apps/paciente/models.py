from django.db import models
from datetime import time, timedelta, datetime
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
        hora_choices.append((hora_actual.strftime('%H:%M'), hora_actual.strftime('%I:%M %p')))
        hora_actual += incremento

    hora = models.CharField(max_length=10, choices=hora_choices)

    def __str__(self):
        return str(self.hora)[0:-3]

class Paciente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=90)
    obra_social = models.CharField(max_length=25, blank=True)
    celular = models.CharField(max_length=12)
    dni = models.IntegerField()
    observaciones = models.TextField(blank=True)
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    hora = models.ForeignKey(Hora, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

