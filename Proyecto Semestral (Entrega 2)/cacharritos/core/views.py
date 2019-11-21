from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Arriendo
from .forms import Arriendoform
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def vehiculos(request):
    return render(request, 'core/vehiculos.html')

def contacto(request):
    return render(request, 'core/contacto.html')

@login_required   ##
def arriendos(request):
    
    arriendos = Arriendo.objects.all() ##
    data={

        'arriendos':arriendos
    }

    return render(request, 'core/arriendo.html',data)

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



def nuevo_arriendo (request):

    data = {
        'form':Arriendoform()
    }
    return(render,'core/nuevo_arriendo.html', data)
