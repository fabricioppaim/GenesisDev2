from django.db import models

class Ambiente(models.Model):
    name = models.CharField(max_length=100)
    sufixo = models.CharField(max_length=10)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.name
