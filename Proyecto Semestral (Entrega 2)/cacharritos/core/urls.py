from django.urls import path
from .views import home, vehiculos, contacto, arriendos,registro_usuario,admin,listado,modificar_Arriendo,eliminar

urlpatterns = [    
    path('', home, name="home"),
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('contacto/', contacto, name="contacto"),
    path('arriendos/', arriendos, name="arriendos"),
    path('registro/',registro_usuario, name="Registro_usuario" ),
    path('admin/',admin,name="admin"),
    path('listado/',listado,name="listado"),
    path('modificar_Arriendo/<id>/',modificar_Arriendo,name="modificar_Arriendo"),
    path('eliminar/<id>/', eliminar,name="eliminar_Arriendo")
    
]