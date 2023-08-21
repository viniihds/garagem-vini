from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer
from garagem.models.veiculo import Veiculo

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__",
        foto_attachment_key = SlugRelatedField(source ="foto", queryset =Image.objects.all(), slug_field="attachment_key", required= False, write_only=True
        ) 

class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1
        foto = ImageSerializer(required=False)

class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = 'modelo', 'id', 'preco'