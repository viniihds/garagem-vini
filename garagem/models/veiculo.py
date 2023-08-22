from django.db import models

from garagem.models import Acessorio, Cor, Modelo

from  uploader.models import Image


class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null= True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null= True, default=0)
    descricao = models.CharField(max_length=500, default="")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    acessorio = models.ManyToManyField(Acessorio, related_name="veiculos")
    foto = models.ManyToManyField(Image, related_name="+", default=None)

    def __str__(self):
        return f"{self.modelo}({self.cor}, {self.ano})"
    class Meta:
        verbose_name = "veículo"