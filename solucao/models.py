from django.db import models


class Cidadao(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    data_nasc = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.cpf


class Estudante(models.Model):
    instituicao = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    
    def __str__(self):
        return self.matricula



class PasseLivre(models.Model):
    codigo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.codigo