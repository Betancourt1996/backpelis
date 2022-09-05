from ast import Str
from django.db import models
class Generos(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'generos'


class Usuarios(models.Model):
    usuario = models.CharField(max_length=255, blank=True, null=True)
    contra = models.CharField(max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'



class Opinions(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'opinions'
