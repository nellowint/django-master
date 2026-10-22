
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de criação'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de atualização'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Ativo'
    )

    class Meta:
        abstract = True
