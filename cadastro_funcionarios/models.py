from django.db import models

# Create your models here.

class Posicao(models.Model):
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

class Funcionarios(models.Model):
    nomeCompleto = models.CharField(max_length = 100)
    matricula = models.CharField(max_length = 8)
    fone = models.CharField(max_length = 11)
    posicao = models.ForeignKey(Posicao, on_delete = models.CASCADE)
    