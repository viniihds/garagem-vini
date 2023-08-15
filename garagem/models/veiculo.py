from django.db import models
from .marca import Marca
from .cor import Cor
from .categoria import Categoria

class Veiculo(models.Model):
    modelo = models.CharField(max_length=150, default= "")
    ano = models.IntegerField(null= True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null= True, default=0)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")

    def __str__(self):
        return f"{self.modelo}({self.cor}, {self.marca}, {self.ano})"
    class Meta:
        verbose_name = "veículo"