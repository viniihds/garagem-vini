from rest_framework.serializers import ModelSerializer

from garagem.models.modelo import Modelo
class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"