from operator import truediv
from pyexpat import model
from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
class Flora(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50)
    valor = models.IntegerField()
    disponibilidad = models.BooleanField()
    imagen = models.ImageField(upload_to="floras", null=True)
    
    def __str__(self):
        return self.nombre
    

    
    