from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.CharField(max_length=7)
    validade = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.nome