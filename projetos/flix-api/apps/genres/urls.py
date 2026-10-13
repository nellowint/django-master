
from django.urls import path
from .views import *

app_name = 'genres'

urlpatterns = [
    path('', list_view_genres, name='genres_list')
]
