from rest_framework.serializers import ModelSerializer

from garagem.models import marca, cor, categoria, acessorio

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = marca
        fields = "__all__"

class CorSerializer(ModelSerializer):
    class Meta:
        model = cor
        fields = "__all__"

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = categoria
        fields = "__all__"

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = acessorio
        fields = "__all__"