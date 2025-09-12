from django.db import models

class Credencial(models.Model):
    name = models.CharField(max_length=100)
    cred_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name
