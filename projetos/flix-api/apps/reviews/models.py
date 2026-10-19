
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.movies.models import Movie
from core.models import BaseModel


class Review(BaseModel):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0, 'Não pode ser menor que 0 (zero)'),
            MaxValueValidator(5, 'Não pode ser maior que 5 (cinco)'),
        ],
        verbose_name='Estrelas'
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name='Comentário'
    )

    def __str__(self):
        return f'Filme: {self.movie} - Estrelas: {self.stars}'

    class Meta():
        ordering = ['-created_at']
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'