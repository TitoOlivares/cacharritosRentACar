from django.contrib import admin
from .models import Marca, Automovil, Arriendo

# Register your models here.

class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'agno', 'modelo')
    search_fields = ['patente', 'modelo'] 
    list_filter = ('marca',)  

admin.site.register(Marca)
admin.site.register(Automovil, AutomovilAdmin)
admin.site.register(Arriendo)