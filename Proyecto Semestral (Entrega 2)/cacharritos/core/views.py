from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def vehiculos(request):
    return render(request, 'core/vehiculos.html')

def contacto(request):
    return render(request, 'core/contacto.html')