
from django.contrib import admin

from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthday', 'nationality']
    search_fields = ['name', 'nationality']
