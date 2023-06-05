import calendar
from django import forms
from .models import Paciente, Fecha, Hora
from apps.obra_sociales.models import ObraSocial
import datetime

class PacienteForm(forms.ModelForm):
    
    # hora_choices = [(datetime.time(hour, minute).strftime('%H:%M'), datetime.time(hour, minute).strftime('%I:%M %p')) 
    #                 for hour in range(16, 19) for minute in range(0, 60, 10)]
    # hora_choices = hora_choices[3:]
    # hora_choices.append(('19:00', '07:00 PM'))
    hora = forms.ModelChoiceField(queryset=Hora.objects.all())

    fecha = forms.ModelChoiceField(queryset=Fecha.objects.all())
    obra_social = forms.ModelChoiceField(queryset=ObraSocial.objects.all(), required=False)
    nueva_obra_social = forms.CharField(max_length=100, required=False)
    # dia_choices = [
    #     (datetime.date.today().replace(day=i)).strftime('%Y-%m-%d')
    #     for i in range(1, calendar.monthrange(datetime.date.today().year, datetime.date.today().month)[1] + 1)
    #     if (datetime.date.today().replace(day=i)).weekday() in [1, 3]
    # ]
    # print(dia_choices)

    # fecha = forms.ChoiceField(choices=[(dia, dia) for dia in dia_choices])

    # def obtener_id_fecha(self):
    #     fecha_str = self.cleaned_data['fecha']
    #     fecha = Fecha.objects.get(fecha=fecha_str)
    #     return fecha.id
 


    # def clean(self):
    #     cleaned_data = super().clean()
    #     fecha = cleaned_data.get('fecha')
    #     hora = cleaned_data.get('hora')

    #     if fecha and hora:
    #         turno_existente = Paciente.objects.filter(fecha__fecha=fecha, hora__hora=hora).exists()

    #         if turno_existente:
    #             self.add_error('hora', 'La combinación de fecha y hora ya ha sido asignada como turno.')

    #     return cleaned_data

    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'dni', 'celular', 'observaciones', 'fecha', 'hora', 'obra_social']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'obra_social': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'hora': forms.Select(attrs={'class': 'form-control'}),
        }

