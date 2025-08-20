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
        labels = {
            'telPadre': 'Teléfono del padre',
            'telMadre': 'Teléfono de la madre'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del patinador/a'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos del patinador/a'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Fecha de nacimiento'}),
            'modalidad': forms.Select(attrs={'class': 'form-select'}),
            'padre': forms.TextInput(attrs={'class': 'form-control'}),
            'madre': forms.TextInput(attrs={'class': 'form-control'}),
            'telPadre': forms.TextInput(attrs={'class': 'form-control'}),
            'telMadre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'cuenta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introducir el número de cuenta'}),
        }

