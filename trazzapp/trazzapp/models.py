from django.db import models


class Rol(models.Model):
    nom_rol = models.CharField(max_length=50, unique=True)
