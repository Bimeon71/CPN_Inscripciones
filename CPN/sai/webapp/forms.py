from cProfile import label

from django.forms import EmailInput
from django.forms.fields import CharField
from django.forms.models import ModelForm
from django import forms
from webapp.models import Inscripcion

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'
        exclude = ['cuenta']
        labels = {
            'fecha': 'Fecha de nacimiento',
            'telPadre': 'Teléfono del padre',
            'telMadre': 'Teléfono de la madre',
            'grupoShow': 'Apuntarme a Grupo Show',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del patinador/a'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos del patinador/a'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'modalidad': forms.Select(attrs={'class': 'form-select mb-2'}),
            'grupoShow': forms.CheckboxInput(attrs={'class': 'form-check-input mb-2'}),
            'padre': forms.TextInput(attrs={'class': 'form-control'}),
            'madre': forms.TextInput(attrs={'class': 'form-control'}),
            'telPadre': forms.TextInput(attrs={'class': 'form-control'}),
            'telMadre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control mb-2', 'placeholder': 'Correo electrónico'}),
            #'cuenta': forms.TextInput(attrs={'class': 'form-control disabled', 'placeholder': 'Póngase en contacto con el club para facilitar el número de cuenta'}),
        }

