from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models.marca import Marca
from garagem.serializers.marca import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer