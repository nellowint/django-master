
from django.urls import path
from .views import *

app_name = 'genres'

urlpatterns = [
    path('', view_genres, name='view_genres'),
    path('/<int:pk>/', detail_genres, name='detail_genres')
]
