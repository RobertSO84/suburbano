from django.db import models

# Create your models here.

class Linea(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Estacion(models.Model):
    nombre = models.CharField(max_length=255)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE, related_name='estaciones')
    distancia_anterior = models.FloatField(default=0)
    estacion_anterior = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Viajes(models.Model):
    estacion_entrada = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='entradas')
    hora_inicio = models.DateTimeField(auto_now=False, auto_now_add=False)
    estacion_salida = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='salidas')
    hora_salida = models.DateTimeField(auto_now=False, auto_now_add=False)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE, related_name='viajes')
    
    def __str__(self):
        return self.estacion_entrada, self.estacion_salida


class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nombre



