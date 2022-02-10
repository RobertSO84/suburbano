from django.contrib import admin
from lineas.models import Linea, Estacion, Viajes, Usuario

# Register your models here.
admin.site.register(Linea)
admin.site.register(Estacion)
admin.site.register(Viajes)
admin.site.register(Usuario)