# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=100,validators=[MinLengthValidator(4)] )
    ap_paterno = models.CharField(verbose_name='Apellido paterno', max_length=40,validators=[MinLengthValidator(4)])
    ap_materno = models.CharField(verbose_name='Apellido materno', max_length=40,validators=[MinLengthValidator(4)])
    edad = models.PositiveIntegerField()   
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombre
    