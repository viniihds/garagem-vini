from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import marca, cor, categoria, acessorio, veiculo
from garagem.serializers import MarcaSerializer, CorSerializer, CategoriaSerializer, AcessorioSerializer, VeiculoSerializer, VeiculoDetailSerializer


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

class VeiculoViewSet(ModelViewSet):
    queryset = veiculo.objects.all()
    serializer_class = VeiculoSerializer
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return VeiculoDetailSerializer
        return VeiculoSerializer