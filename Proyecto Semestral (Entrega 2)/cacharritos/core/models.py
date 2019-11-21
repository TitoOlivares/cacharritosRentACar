from django.db import models
from django.contrib.auth.models import User


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
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=10)
    telefono=models.IntegerField()
    correo = models.CharField(max_length=250)
    tarjeta = models.IntegerField()
    duracion = models.IntegerField()
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    auto = models.ForeignKey(Automovil,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Arriendo"
        verbose_name_plural = "Arriendos"
