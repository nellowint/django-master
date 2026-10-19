
from django.db import models

from core.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(
        max_length=200,
        verbose_name='Nome'
    )

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['id']
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
