from django.db import models
from django.utils import timezone
from django import forms



# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Automovil(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    agno = models.IntegerField(verbose_name="año")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
    class Meta:
        verbose_name = "Automovil"
        verbose_name_plural = "Automoviles"

class Arriendo(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(default='', max_length=9)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    fecha_arriendo = models.DateField(blank=False)
    fecha_devolucion = models.DateField(blank=False)
    estado = models.CharField(default='Pendiente', max_length=20)


