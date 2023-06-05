from django.db import models

# Create your models here.
class ObraSocial(models.Model):
    ESTADO_CHOICES = [
        ('ACT', 'Activo'),
        ('SUS', 'Suspendido'),
    ]
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    estado = models.CharField(max_length=100, choices=ESTADO_CHOICES)
    telefono = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre