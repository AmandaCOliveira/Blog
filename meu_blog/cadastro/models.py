from django.db import models

# Create your models here.

class Dados(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    idade = models.CharField(max_length=3)
