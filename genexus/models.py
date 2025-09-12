from django.db import models

class Genexus(models.Model):
    gx_server_url = models.CharField(max_length=200)
    gx_server_version = models.CharField(max_length=20)
    gx_server_working_directory = models.CharField(max_length=200)
    gx_server_working_directory_kb = models.CharField(max_length=200)

    def __str__(self):
        return self.gx_server_url
