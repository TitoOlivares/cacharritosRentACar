from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Arriendo
from django import forms



# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def vehiculos(request):
    return render(request, 'core/vehiculos.html')

def contacto(request):
    return render(request, 'core/contacto.html')

@login_required



def arriendos(request):
    form = ArriendoForm()
    data = {
        'arriendo':ArriendoForm()
    }
    if request.method =='POST':
        formulario = ArriendoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Solicitud enviada correctamente. Pronto nos pondremos en contacto con usted.')
    return render(request, 'core/arriendo.html', {'form': form},data)

class ArriendoForm (forms.ModelForm):
    
    class Meta:
        model = Arriendo
        fields = [
            'nombre_completo','correo','direccion','telefono','marca','modelo','fecha_arriendo',
            'fecha_devolucion']
        widgets = {
            'fecha_arriendo' : forms.DateInput(attrs={'type':'date','id':'fecha_arriendo'}),
            'fecha_devolucion' : forms.DateInput(attrs={'type':'date','id':'fecha_devolucion'})
        }

def admin(request):
    return render(request,'admin')

def registro_usuario (request):
    data= {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username= formulario.cleaned_data ['username']
            password= formulario.cleaned_data ['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(to='home')
    return render(request,'registration/registrar.html',data)

class CustomUserForm(UserCreationForm):

    class Meta:
        model = User 
        fields = ['first_name', 'last_name','email','username','password1','password2']

def listado(request):
    
    arriendos = Arriendo.objects.all() ##
    data={

        'arriendos':arriendos
    }

    return render(request, 'core/listado_solicitudes.html',data)


def modificar_Arriendo(request,id):
    arriendo=Arriendo.objects.get(id=id)
    data={
        'form':ArriendoForm(instance=arriendo)
    }

    if request.method == 'POST':
        formulario = ArriendoForm(data= request.POST,instance=arriendo)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Actualizado Correctamente"
            data['form'] = formulario

    return render(request,'core/actualizar_arriendo.html', data)


def eliminar (request,id):
    arriendo = Arriendo.objects.get(id=id)
    arriendo.delete()
    return redirect (to="listado")     