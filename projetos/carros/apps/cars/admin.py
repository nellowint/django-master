
from django.contrib import admin

from .models import Brand, Car


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'plate',
        'brand',
        'factory_year',
        'model_year',
        'price'
    ]
    search_fields = ['name', 'brand',]
