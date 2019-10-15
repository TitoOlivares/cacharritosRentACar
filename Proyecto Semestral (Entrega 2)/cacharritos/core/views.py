from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def vehiculos(request):
    return render(request, 'core/vehiculos.html')

def contacto(request):
    return render(request, 'core/contacto.html')

@login_required
def arriendos(request):
    return render(request, 'core/arriendo.html')