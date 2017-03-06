from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField()