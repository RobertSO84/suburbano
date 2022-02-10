from lineas.models import Linea, Estacion, Viajes, Usuario
from rest_framework import serializers

class LineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linea
        fields = ('nombre', 'ubicacion')


class EstacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estacion
        fields = ('nombre', 'linea', 'distancia_anterior')

class ViajesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Viajes
        fields = ('estacion_entrada', 'estacion_salida', 'hora_inicio', 'hora_salida')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellidos', 'viajes')

