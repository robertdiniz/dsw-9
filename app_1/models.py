from django.db import models

# Create your models here.
class Disco(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=250)
    pais = models.CharField(max_length=50)
    quantidade = models.IntegerField()
