from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

class Empresa(models.Model):
    nome = models.CharField(max_length=250)
    

class Funcionario(models.Model):
    nome = models.CharField(max_length=250)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
  

class Fila(models.Model):
    descricao = models.CharField(max_length=250)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)


class FilaPosicao(models.Model):
    fila = models.ForeignKey(Fila, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posicao = models.IntegerField()




