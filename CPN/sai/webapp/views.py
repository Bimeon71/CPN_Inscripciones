from django.forms.models import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

from webapp.forms import InscripcionForm
from webapp.models import Inscripcion


# Create your views here.
#InscripcionForm = modelform_factory(Inscripcion, exclude=[])
def nuevaInscripcion(request):
    #return HttpResponse("Club Patinaje Nájera. Temporada 2025-2026")
    #return  render(request, 'nuevo.html')
    if request.method == 'POST':
        formNuevo = InscripcionForm(request.POST)
        if formNuevo.is_valid():
            formNuevo.save()
            return redirect('index')
    else:
        formNuevo = InscripcionForm()
    return render(request, 'nuevo.html', {'formNuevo': formNuevo})
    #return render(request, 'confirmacion.html')

# def confirmarInscripcion(request):
#     return render(request, 'confirmacion.html')

