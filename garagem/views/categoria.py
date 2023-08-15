from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models.categoria import Categoria
from garagem.serializers.categoria import CategoriaSerializer
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer