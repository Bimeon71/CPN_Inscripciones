from django.db import models

OPCIONES_MOD = [
    (1, 'Iniciación/extraescolar'),
    (2, 'Competición 2 días'),
    (3, 'Competición 3 días'),
    #(4, 'Grupo Show (1 hora semanal)'),
]
# Create your models here.
class Inscripcion(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=500)
    fecha = models.DateField()
    #modalidad = models.CharField(max_length=2)
    modalidad = models.IntegerField(choices=OPCIONES_MOD, default=2)
    grupoShow = models.BooleanField(default=False)
    padre = models.CharField(max_length=100)
    madre = models.CharField(max_length=100)
    telPadre = models.CharField(max_length=15)
    telMadre = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    cuenta = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}.- {self.nombre} {self.apellidos}'
