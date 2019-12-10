from django.db import models

# Create your models here.

class Post(models.Model):
    opcao_tema= [
        ('ROM', 'Romance'),
        ('GUM', 'Games'),
        ('LIM', 'Algoritmo'),
    ]
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(default=1)
    email = models.CharField(max_length=50)
    texto_blog = models.CharField(max_length=150)
    tema = models.CharField(max_length=3, choices=opcao_tema)
    ativo = models.BooleanField(default=True)
