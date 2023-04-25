from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import marca, cor, categoria, acessorio
from garagem.serializers import MarcaSerializer, CorSerializer, CategoriaSerializer, AcessorioSerializer


class MarcaViewSet(ModelViewSet):
    queryset = marca.objects.all()
    serializer_class = MarcaSerializer


class CorViewSet(ModelViewSet):
    queryset = cor.objects.all()
    serializer_class = CorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class AcessorioViewSet(ModelViewSet):
    queryset = acessorio.objects.all()
    serializer_class = AcessorioSerializer
