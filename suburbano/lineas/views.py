#from django.http import JsonResponse
#from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
#from rest_framework.response import Response
from lineas.serializers import LineaSerializer, EstacionSerializer, ViajesSerializer, UsuarioSerializer
#from django.views.generic import View
from lineas.models import Linea, Estacion, Viajes, Usuario

# Create your views here.
class LineaView(ModelViewSet):
    queryset = Linea.objects.all().order_by('id')
    serializer_class = LineaSerializer

class EstacionView(ModelViewSet):
    queryset = Estacion.objects.all().order_by('id')
    serializer_class = EstacionSerializer

class ViajesView(ModelViewSet):
    queryset = Viajes.objects.all().order_by('id')
    serializer_class = ViajesSerializer

class UsuarioView(ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer





# class LineaView(APIView):
#     def get(self, request):
#         lineas = Linea.objects.all().values_list('id', 'nombre')
#         return Response({'lineas': list(lineas)})

# class EstacionView(APIView):
#     def get(self, request, linea):
#         estaciones = Estacion.objects.filter(linea=linea).values('id', 'nombre')
#         return Response({'estaciones': estaciones})


        