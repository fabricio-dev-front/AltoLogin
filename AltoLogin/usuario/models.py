from django.db import models
from django import forms

# Create your models here.
class Usuario(models.Model):
    email = models.EmailField(primary_key = True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    genero = models.CharField(max_length=11)
    dataNascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    
