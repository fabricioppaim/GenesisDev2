from django.db import models
from ambientes.models import Ambiente

class LogGenexus(models.Model):
    conversion_pattern = models.TextField()
    ambientes = models.ManyToManyField(Ambiente)

    def __str__(self):
        return self.conversion_pattern[:30]
