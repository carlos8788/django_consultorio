from django.db import models

# Create your models here.
class ObraSocial(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Active'),
        ('Suspendido', 'Suspended'),
    ]
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    estado = models.CharField(max_length=100, choices=ESTADO_CHOICES)
    telefono = models.CharField(max_length=100)
    
    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            # Agrega otros campos relevantes
        }
    def __str__(self):
        return self.nombre