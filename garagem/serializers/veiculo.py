from rest_framework.serializers import ModelSerializer

from garagem.models.veiculo import Veiculo

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"

class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1

class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = 'modelo', 'id', 'preco'