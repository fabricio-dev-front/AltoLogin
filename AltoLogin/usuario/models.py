from django.db import models
from django import forms

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    genero = models.CharField(max_length=11)
    dataNascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    
