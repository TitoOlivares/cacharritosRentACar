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
            'username',
            'last_name',
            'email',
            'first_name',
            'password1',
            'password2'
        ]
        

class ArriendoForm (forms.ModelForm):
    
    class Meta:
        model = Arriendo
        fields = [
            'nombre_completo',
            'correo',
            'direccion',
            'telefono',
            'marca',
            'modelo',
            'fecha_arriendo',
            'fecha_devolucion',
        ]
        widgets = {
            'fecha_arriendo' : forms.DateInput(attrs={'type':'date','id':'fecha_arriendo'}),
            'fecha_devolucion' : forms.DateInput(attrs={'type':'date','id':'fecha_devolucion'})
        }