
from core.model import BaseModel
from django.db import models


class Brand(BaseModel):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Marca'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class Car(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    plate = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Placa',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='cars/',
        verbose_name='Imagem',
        blank=True,
        null=True
    )
    factory_year = models.PositiveIntegerField(
        verbose_name='Ano de Fabricação',
        blank=True,
        null=True
    )
    model_year = models.PositiveIntegerField(
        verbose_name='Ano do Modelo',
        blank=True,
        null=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Preço',
        blank=True,
        null=True
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        verbose_name='Marca',
        related_name='brands'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

