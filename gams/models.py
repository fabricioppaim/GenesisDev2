from django.db import models
from ambientes.models import Ambiente

class GAM(models.Model):
    user_id_gam_admin = models.CharField(max_length=100)
    user_id_gam_connection = models.CharField(max_length=100)
    ambientes = models.ManyToManyField(Ambiente)

    def __str__(self):
        return self.user_id_gam_admin
