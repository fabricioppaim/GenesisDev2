from django.db import models
from ambientes.models import Ambiente

class Web(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100, blank=True)
    shared = models.CharField(max_length=100, blank=True)
    ambientes = models.ManyToManyField(Ambiente)
    finalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.name
