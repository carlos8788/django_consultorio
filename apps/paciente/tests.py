from django.test import TestCase
from datetime import datetime, timedelta, date
from .models import Hora, Fecha

def datos():

    # Definir la fecha de inicio
    fecha_inicio = date(2023, 6, 6)

    # Definir la fecha de fin
    fecha_fin = date(2023, 6, 29)

    # Crear una lista para almacenar las fechas de los martes y jueves
    fechas_martes_jueves = []

    # Iterar sobre los días entre la fecha de inicio y la fecha de fin
    delta = timedelta(days=1)
    fecha_actual = fecha_inicio

    while fecha_actual <= fecha_fin:
        if fecha_actual.weekday() in [1, 3]:  # 1 representa el martes, 3 representa el jueves
            fechas_martes_jueves.append(fecha_actual)
        fecha_actual += delta

    # Imprimir las fechas de los martes y jueves
    for fecha in fechas_martes_jueves:
        print(fecha)
        dates = Fecha(fecha=fecha)
        # dates.save()
    