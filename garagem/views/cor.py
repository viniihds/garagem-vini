from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models.cor import Cor
from garagem.serializers.cor import CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer