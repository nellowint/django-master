
from django.db import models
from django_countries.fields import CountryField

from core.models import BaseModel


class Actor(BaseModel):
    name = models.CharField(
        max_length=200,
        verbose_name='Nome'
    )
    birthday = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Nascimento'
    )
    nationality = CountryField(
        blank=True,
        null=True,
        verbose_name='Nacionalidade',
        blank_label='Selecione o país'
    )

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['name']
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'

