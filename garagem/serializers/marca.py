from rest_framework.serializers import ModelSerializer

from garagem.models.marca import Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"