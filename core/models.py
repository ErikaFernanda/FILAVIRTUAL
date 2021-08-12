from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

class Empresa(models.Model):
    nome = models.CharField(max_length=250)
    def __self__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=250)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    def __self__(self):
        return self.empresa+" "+self.nome

class Fila(models.Model):
    descricao = models.CharField(max_length=250)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    def __self__(self):
        return self.descricao

class FilaPosicao(models.Model):
    fila = models.ForeignKey(Fila, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posicao = models.IntegerField()
    def __self__(self):
        return self.usuario.nome+"  "+self.posicao



