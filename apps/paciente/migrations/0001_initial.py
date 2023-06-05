# Generated by Django 4.2.1 on 2023-06-04 22:08

from django.db import migrations
from datetime import datetime, timedelta
def cargar_datos(apps, schema_editor):
    Hora = apps.get_model('paciente', 'Hora')
    hora_choices = []
    hora_inicio = datetime.strptime('16:30', '%H:%M').time()  # Hora de inicio: 16:30
    hora_fin = datetime.strptime('19:00', '%H:%M').time()  # Hora de fin: 19:00
    incremento = timedelta(minutes=10)  # Incremento de 10 minutos

    hora_actual = datetime.combine(datetime.today(), hora_inicio)

    while hora_actual.time() <= hora_fin:
        hora_choices.append((hora_actual.strftime('%H:%M'), hora_actual.strftime('%I:%M %p')))
        hora_actual += incremento

    # hora_choices = [...]  # Aquí van tus opciones de hora generadas
    Hora.objects.bulk_create(hora_choices)

class Migration(migrations.Migration):

    dependencies = [
        # Dependencias de otras migraciones, si las hay
    ]

    operations = [
        migrations.RunPython(cargar_datos),
    ]