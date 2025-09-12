from django.db import models

class Empresa(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.name
