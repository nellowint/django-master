
from django.db import models

from apps.actors.models import Actor
from apps.genres.models import Genre
from core.models import BaseModel


class Movie(BaseModel):
    title = models.CharField(
        max_length=500,
        verbose_name='Título'
    )
    sinopse = models.TextField(
        blank=True,
        null=True,
        verbose_name='Sinopse do Filme'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies'
    )
    release_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Lançamento'
    )
    actors = models.ManyToManyField(
        Actor,
        related_name='movies'
    )

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['-created_at']
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'