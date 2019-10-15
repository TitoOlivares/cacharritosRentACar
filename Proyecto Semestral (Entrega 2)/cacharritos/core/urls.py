from django.urls import path
from .views import home, vehiculos, contacto

urlpatterns = [    
    path('', home, name="home"),
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('contacto/', contacto, name="contacto"),
]