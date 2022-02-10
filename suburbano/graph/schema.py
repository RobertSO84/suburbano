import graphene
from django import forms
from lineas.models import Linea, Estacion, Usuario, Viajes 
from graphene_django  import DjangoObjectType
from graphene_django.forms.mutation  import DjangoFormMutation

class LineaType(DjangoObjectType):
    class Meta:
        model = Linea
        fields = ("id", "nombre", "ubicacion", "estaciones")

class LineaForm(forms.Form):
    nombre = forms.CharField()
    ubicacion = forms.CharField()

class LineaMutation(DjangoFormMutation):
    class Meta:
        form_class = LineaForm


class EstacionType(DjangoObjectType):
    class Meta:
        model = Estacion
        fields = ("id", "nombre", "linea", "distancia_anterior")

class ViajesType(DjangoObjectType):
    class Meta:
        model = Viajes
        fields = ("estacion_entrada", "estacion_salida", "hora_inicio", "hora_salida")

class UsuarioType(DjangoObjectType):
    class Meta:
        model = Usuario
        fields = ("nombre", "apellidos", "viajes")


class Query(graphene.ObjectType):
    lineas = graphene.List(LineaType)
    estaciones = graphene.List(EstacionType)
    viajes = graphene.List(ViajesType)
    usuarios = graphene.List(UsuarioType)

    def resolve_lineas(root, info):
        return Linea.objects.all()

    def resolve_estaciones(root, info):
        return Estacion.objects.all()

    def resolve_viajes(root, info):
        return Viajes.objects.all()

    def resolve_usuarios(root, info):
        return Usuario.objects.all()
    
class Mutation(graphene.ObjectType):
    create_linea = LineaMutation.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)