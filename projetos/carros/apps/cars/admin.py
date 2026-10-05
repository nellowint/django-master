
from django.contrib import admin
from .models import *


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand']
    search_fields = ['name', 'brand__name']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'model__brand', 'factory_year', 'model_year', 'price']
    search_fields = ['name', 'model__name', 'model__brand__name']
