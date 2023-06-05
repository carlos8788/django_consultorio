from django.test import TestCase
import json
from .models import ObraSocial
# Create your tests here.
def datos():
    # import json

# Abrir el archivo json para leerlo
    with open('all.json', 'r') as f:
        data = json.load(f)

    # Ahora "data" contiene los datos del archivo json
    for i in data:
        obra_social = {}
        obra_social['nombre'] = i['cnomosoc'].strip() 
        obra_social['direccion'] = i['cdomosoc'].strip() + ", " +  i['clocosoc'].strip()
        # obra_social['telefono'] = i['ctelosoc']
        obra_social['estado'] = i['estA_OSOC']['crefestaosoc'].strip()
        if i['ctelosoc'] is not None:
            print('not none')
            obra_social['telefono'] = i['ctelosoc'].strip()
        else:
            obra_social['telefono'] = '---'
        print(obra_social)
        nueva_obra_social = ObraSocial(**obra_social)
        nueva_obra_social.save()


    pass