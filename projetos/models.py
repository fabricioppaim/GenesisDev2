from django.db import models

class Projeto(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    server_kb_alias = models.CharField(max_length=100)
    kb_version = models.CharField(max_length=50)
    target_path = models.CharField(max_length=100)
    arquivos_complementares = models.CharField(max_length=100, blank=True)
    exclude_files = models.CharField(max_length=200, blank=True)
    directory_config_msbuild = models.CharField(max_length=200, blank=True)
    base_gam = models.BooleanField(default=False)
    https = models.BooleanField(default=False)

    def __str__(self):
        return self.name
