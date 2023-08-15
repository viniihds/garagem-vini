from django.db import models
from .marca import Marca
from .categoria import Categoria

class Modelo(models.Model):
    nome = models.CharField(max_length=150, default= "")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="modelos")

    def __str__(self):
        return f"{self.marca}{self.nome}"
    class Meta:
        verbose_name = "Modelo"