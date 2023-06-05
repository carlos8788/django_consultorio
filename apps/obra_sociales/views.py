from .models import ObraSocial
from django.shortcuts import render

def view_public(request):
    obras_sociales = ObraSocial.objects.all()
    return render(request, 'pages/obra_sociales.html', {'obras_sociales': obras_sociales})
