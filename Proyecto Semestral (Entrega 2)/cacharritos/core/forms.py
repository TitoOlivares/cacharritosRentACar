from django import forms
from django.forms import ModelForm
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Arriendo

class CustomUserForm (UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]

class Arriendoform(ModelForm):
    class Meta:

        model = Arriendo
        fields =[
            'nombre',
            'apellido',
            'rut',
            'telefono',
            'correo',
            'tarjeta',
            'duracion',
            'usuario',
            'auto'
        ]