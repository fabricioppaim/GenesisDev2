from django.db import models
from ambientes.models import Ambiente

class BancoDeDados(models.Model):
    name = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100, blank=True)
    engine = models.CharField(max_length=50)
    ambientes = models.ManyToManyField(Ambiente)

    def __str__(self):
        return self.name

class BancoDados(models.Model):
    banco_de_dados = models.ForeignKey(BancoDeDados, related_name='bancos', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    user_id_jenkis = models.CharField(max_length=100)

    def __str__(self):
        return self.name
