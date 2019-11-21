from django.urls import path
from .views import home, vehiculos, contacto, arriendos,registro_usuario, nuevo_arriendo

urlpatterns = [    
    path('', home, name="home"),
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('contacto/', contacto, name="contacto"),
    path('arriendos/', arriendos, name="arriendos"),
    path('registro/',registro_usuario, name="Registro_usuario" ),
    path('nuevo_arriendo/',nuevo_arriendo,name="nuevo_arriendo"),
]