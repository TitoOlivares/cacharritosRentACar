from django.contrib import admin
from .models import Marca, Automovil,Arriendo

# Register your models here.

class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'agno', 'modelo')
    search_fields = ['patente', 'modelo'] 
    list_filter = ('marca',)  


class ArriendoAdmin(admin.ModelAdmin):
    list_display =('nombre', 'apellido', 'rut', 'telefono', 'correo', 'tarjeta', 'duracion', 'auto', 'usuario' )
    search_fields =('nombre','rut', 'usuario')
    list_filter =('auto',)
    list_per_page = 15


admin.site.register(Arriendo,ArriendoAdmin)
admin.site.register(Marca)
admin.site.register(Automovil, AutomovilAdmin)