from django.db import models

class marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.nome.upper()
    class Meta:
        verbose_name = "marca"

class categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name = "categoria"

class acessorio(models.Model):
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name = "acessório"

class cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name_plural = "Cores"
        verbose_name = "cor"

class veiculo(models.Model):
    modelo = models.CharField(max_length=150, default= "")
    ano = models.IntegerField(null= True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null= True, default=0)
    marca = models.ForeignKey(marca, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(cor, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(categoria, on_delete=models.PROTECT, related_name="veiculos")

    def __str__(self):
        return f"{self.modelo}({self.cor}, {self.marca}, {self.ano})"
    class Meta:
        verbose_name = "veículo"